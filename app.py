import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import firestore
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
st.write('Hell')
