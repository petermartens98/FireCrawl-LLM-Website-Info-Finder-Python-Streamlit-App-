import streamlit as st
from firecrawl import FirecrawlApp
from pydantic import create_model

FIELD_TYPES = {"String": str, "Number": float, "Boolean": bool}

def create_dynamic_schema(fields: dict) -> type:
    return create_model('DynamicSchema', **{name: (type_, ...) for name, type_ in fields.items()})

def main():
    st.title("FireCrawl LLM Website Info Finder")
    
    # API Key input
    api_key = st.text_input("Enter Firecrawl API Key", type="password")
    if not api_key:
        st.warning("Please enter your API key to proceed.")
        return
    
    app = FirecrawlApp(api_key=api_key)
    
    # URL input for multiple websites
    urls_input = st.text_area("URLs to scrape (one per line)", help="Enter each URL on a new line")
    urls = [url.strip() for url in urls_input.splitlines() if url.strip()]
    
    # Schema setup
    st.subheader("Extraction Schema")
    if 'fields' not in st.session_state:
        st.session_state.fields = {}
    
    with st.form('schema_form'):
        temp_fields = []
        while True:
            col1, col2 = st.columns(2)
            name = col1.text_input("Field name", key=f"name_{len(temp_fields)}")
            type_ = col2.selectbox("Type", list(FIELD_TYPES), key=f"type_{len(temp_fields)}")
            if not name:
                break
            temp_fields.append((name, type_))
        
        col1, col2 = st.columns(2)
        submit = col1.form_submit_button("Update Schema")
        if submit and temp_fields:
            names = [n for n, _ in temp_fields]
            if len(names) == len(set(names)):
                st.session_state.fields = {n: FIELD_TYPES[t] for n, t in temp_fields}
                st.success("Schema updated!")
            else:
                st.warning("Duplicate field names detected!")

    # Display schema
    if st.session_state.fields:
        st.subheader("Current Schema")
        for name, type_ in st.session_state.fields.items():
            st.write(f"- {name}: {type_.__name__}")
        if st.button("Clear Schema"):
            st.session_state.fields = {}
            st.rerun()

    # Scrape multiple URLs
    if urls and st.session_state.fields and st.button("Scrape URLs"):
        with st.spinner("Scraping multiple URLs..."):
            try:
                schema = create_dynamic_schema(st.session_state.fields)
                results = {}
                for url in urls:
                    try:
                        data = app.scrape_url(url, {
                            'formats': ['json'],
                            'jsonOptions': {'schema': schema.model_json_schema()}
                        })
                        results[url] = data["json"]
                    except Exception as e:
                        results[url] = {"error": str(e)}
                
                st.success("Scraping completed!")
                st.subheader("Extracted Data from Multiple URLs")
                st.json(results)
            except Exception as e:
                st.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
