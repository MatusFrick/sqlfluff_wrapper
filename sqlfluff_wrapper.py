import streamlit as st
import sqlfluff
import json


st.set_page_config(layout="wide")
st.title('SQLFluff wrapper')

st.write("Wrapper using [SQLFluff](https://docs.sqlfluff.com/en/stable/) with custom .sqlfluff config and snowflake dialect.")

col1, col2 = st.columns(2, gap="medium")

col1.header("Your code goes here:")
col2.header("Here is your code back:")
col2.write("")
txt = col1.text_area("SQL input", label_visibility="hidden",height=500)

fix_result = sqlfluff.fix(txt, dialect="snowflake", config_path="./.sqlfluff" )
lint_result = sqlfluff.lint(fix_result, dialect="snowflake", config_path="./.sqlfluff" )
lint_str = json.dumps(lint_result, indent=4)


col2.code(f'{fix_result}', line_numbers=True)
st.divider()
st.header("Problems I could not fix:")
st.code(f'{lint_str}')
