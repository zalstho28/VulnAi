#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import pandas as pd


# In[2]:


binary_model_pipeline = pickle.load(open('final_model.pkl', 'rb'))        # Binary classification model (attack or not)
attack_model_pipeline = pickle.load(open('attack_model.pkl', 'rb')) 


# In[3]:


st.title("Web Traffic Log Classification")


# In[4]:


st.subheader("Enter the details for prediction:")


# In[5]:


http_method = st.selectbox('HTTP Method', ['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD'])


# In[6]:


status_code = st.number_input('Status Code', min_value=100, max_value=599, step=1)


# In[7]:


user_agent = st.text_input('User Agent String', 'Mozilla/5.0')


# In[8]:


content_type = st.selectbox('Content Type', [
    'text/html; charset=utf-8',
    'application/json; charset=utf-8',
    'application/xml; charset=utf-8',
    'text/plain; charset=utf-8',
    'application/javascript; charset=utf-8',
    'text/css; charset=utf-8',
    'image/png',
    'image/jpeg'
])


# In[9]:


response_time = st.number_input('Response Time (in seconds)', min_value=0.0, step=0.01)


# In[10]:


content_length = st.number_input('Content Length', min_value=0, step=1)


# In[11]:


referrer = st.text_input('Referrer', 'https://example.com')


# In[12]:


input_data = {
    'http_method': [http_method],
    'status_code': [status_code],
    'user_agent': [user_agent],
    'content_type': [content_type],
    'response_time': [response_time],
    'content_length': [content_length],
    'referrer': [referrer]
}


# In[13]:


input_df = pd.DataFrame(input_data)


# In[20]:


if st.button('Predict'):
    prediction = binary_model_pipeline.predict(input_df)
    if prediction[0] == 1:
            st.write("The predicted label is: **Attack Detected**")
            attack_type_prediction = attack_model_pipeline.predict(input_df)
            st.write(f"Type of attack based on OWASP category: **{attack_type_prediction[0]}**")
    else:
            st.write("The predicted label is: **No Attack Detected**")


# In[ ]:





# In[ ]:




