#!/usr/bin/env python
# coding: utf-8

# # <center> 441b HW7 <center>

# # <center> Yihan Li <center>

# In[2]:


pip install openai wikipedia


# In[3]:


import openai
import os
import wikipedia


# # 1.) Set up OpenAI and the enviornment
# 

# # DONE

# In[4]:


apikey = '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'


# In[5]:


client = openai.OpenAI(
    api_key = apikey)


# # 2.) Use the wikipedia api to get a function that pulls in the text of a wikipedia page

# In[6]:


page_titles = ["Artificial Intelligence","UCLA"]


# In[8]:


def get_wikipedia_content(page_title):
    search_results = wikipedia.search(page_title)
    page = wikipedia.page(search_results[0])
    return(page.content)


# # 3.) Build a chatgpt bot that will analyze the text given and try to locate any false info

# In[9]:


content = get_wikipedia_content(page_titles)


# In[10]:


def chatgpt_error_collection(text):
    chat_completions = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"system","content":"I am looking for false information. If there is even small potential false information, please return it."},
                {"role":"user","content":content[:8180]}]
    )
    print(chat_completions.choices[0].message.content)


# # 4.) Make a for loop and check a few wikipedia pages and return a report of any potentially false info via wikipedia

# In[11]:


for page_title in page_titles:
    try:
        print("_____"+page_title+"_____")
        content = get_wikipedia_content(page_title)
        chatgpt_error_collection(content)
    except:
        print("error")


# # <center> Thanks for Reading <center>
