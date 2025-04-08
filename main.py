# import pandas as pd
# import zipfile
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns
# import requests
# from io import BytesIO
# # import plotly.graph_objects as go
# # from plotly.subplots import make_subplots
# # from my_plots import *
# import streamlit as st

# ## LOAD DATA DIRECTLY FROM SS WEBSITE
# # @st.cache_data
# # def load_name_data():
# #     names_file = 'https://www.ssa.gov/oact/babynames/names.zip'
# #     response = requests.get(names_file)
# #     with zipfile.ZipFile(BytesIO(response.content)) as z:
# #         dfs = []
# #         files = [file for file in z.namelist() if file.endswith('.txt')]
# #         for file in files:
# #             with z.open(file) as f:
# #                 df = pd.read_csv(f, header=None)
# #                 df.columns = ['name','sex','count']
# #                 df['year'] = int(file[3:7])
# #                 dfs.append(df)
# #         data = pd.concat(dfs, ignore_index=True)
# #     data['pct'] = data['count'] / data.groupby(['year', 'sex'])['count'].transform('sum')
# #     return data

# ## LOAD DATA FROM A SAVED FILE
# # df = pd.read_csv('all_names.csv')
# # df['total_births'] = df.groupby(['year', 'sex'])['count'].transform('sum')
# # df['prop'] = df['count'] / df['total_births']

# ## LOAD DATA FROM A SMALLER NAME DATASET ON GITHUB
# url = 'https://raw.githubusercontent.com/esnt/Data/refs/heads/main/Names/popular_names.csv'
# df = pd.read_csv(url)
# df['total_births'] = df.groupby(['year', 'sex'])['n'].transform('sum')
# df['prop'] = df['n'] / df['total_births']

# st.title('My Name App')


# # pick a name
# noi = st.text_input('Enter a name')
# plot_female = st.checkbox('Plot female line')
# plot_male = st.checkbox('Plot male line')
# name_df = df[df['name']==noi]

# fig = plt.figure(figsize=(15, 8))

# if plot_female:
#     sns.lineplot(data=name_df[name_df['sex'] == 'F'], x='year', y='prop', label='Female')

# if plot_male:
#     sns.lineplot(data=name_df[name_df['sex'] == 'M'], x='year', y='prop', label='Male')

# plt.title(f'Popularity of {noi} over time')
# plt.xlim(1880, 2025)
# plt.xlabel('Year')
# plt.ylabel('Proportion')
# plt.xticks(rotation=90)
# plt.legend()
# plt.tight_layout()

# st.pyplot(fig)





import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import BytesIO
import streamlit as st

## LOAD DATA DIRECTLY FROM SS WEBSITE
@st.cache_data
def load_name_data():
    names_file = 'https://www.ssa.gov/oact/babynames/names.zip'
    response = requests.get(names_file)
    with zipfile.ZipFile(BytesIO(response.content)) as z:
        dfs = []
        files = [file for file in z.namelist() if file.endswith('.txt')]
        for file in files:
            with z.open(file) as f:
                df = pd.read_csv(f, header=None)
                df.columns = ['name','sex','count']
                df['year'] = int(file[3:7])
                dfs.append(df)
        data = pd.concat(dfs, ignore_index=True)
    data['pct'] = data['count'] / data.groupby(['year', 'sex'])['count'].transform('sum')
    return data

df = load_name_data()



df['total_births'] = df.groupby(['year', 'sex'])['count'].transform('sum')
df['prop'] = df['count'] / df['total_births']
st.title('My Name App')

tab1, tab2, tab3 = st.tabs(['Overall', 'By Name', 'By Year'])

with tab1:
    st.write('Stuff')
    # noi = st.text_input('Enter a name')
    # name_data = df[df['name'] == noi]
    # sex_counts = name_data.groupby('sex').sum()['count']
    # male_count = sex_counts.get('M', 0)
    # female_count = sex_counts.get('F', 0)
    # total_count = male_count + female_count

    # if total_count > 0:
    #     male_ratio = male_count / total_count
    #     female_ratio = female_count / total_count

    #     fig, ax = plt.subplots(figsize=(10, 2))

    #     # Create a stacked bar representing male and female ratios
    #     ax.barh(0, male_ratio,  label='Male')
    #     ax.barh(0, female_ratio, left=male_ratio,  label='Female')

    #     # Customize the chart
    #     ax.set_xlim(0, 1)
    #     ax.set_xticks([0, 0.5, 1])
    #     ax.set_xticklabels(['0%', '50%', '100%'])
    #     ax.set_yticks([])  # Hide y-axis ticks

    #     # Add labels to display the ratios
    #     ax.text(male_ratio / 2, 0, f"{male_ratio * 100:.1f}%", va='center', 
    #             ha='center', color='white', 
    #             fontweight='bold',
    #             fontsize=20)
    #     ax.text(male_ratio / 2, -.25, "male", va='center', 
    #             ha='center', color='white', 
    #             fontweight='bold',
    #             fontsize=20)
    #     ax.text(male_ratio + female_ratio / 2, 0, f"{female_ratio * 100:.1f}%", va='center', 
    #             ha='center', color='white', 
    #             fontweight='bold',
    #             fontsize=20)
    #     ax.text(male_ratio + female_ratio / 2, -.25, "female", va='center', 
    #             ha='center', color='white', 
    #             fontweight='bold',
    #             fontsize=20)
    #     plt.title(f"Sex Balance of the '{noi}' (over all years)")
    #     plt.show()

with tab2:
    st.write('Name')

    # pick a name
    noi = st.text_input('Enter a name')
    plot_female = st.checkbox('Plot female line')
    plot_male = st.checkbox('Plot male line')
    name_df = df[df['name']==noi]

    fig = plt.figure(figsize=(15, 8))

    if plot_female:
        sns.lineplot(data=name_df[name_df['sex'] == 'F'], x='year', y='prop', label='Female')

    if plot_male:
        sns.lineplot(data=name_df[name_df['sex'] == 'M'], x='year', y='prop', label='Male')

    plt.title(f'Popularity of {noi} over time')
    plt.xlim(1880, 2025)
    plt.xlabel('Year')
    plt.ylabel('Proportion')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()

    st.pyplot(fig)

with tab3:
    st.write('Year')

    # write a year
    yoi = st.text_input('Enter a year')
    plot_female = st.checkbox('Female Plot')
    plot_male = st.checkbox('Male Plot')

    year_of_interest = yoi
    top_names = df[df['year'] == year_of_interest]

    fig = plt.figure(figsize=(10,5))


    if plot_female:
        category  = "Female"
        top_female = top_names[top_names['sex'] == 'F'].nlargest(10, 'count')
        sns.barplot(data=top_female, x='count', y='name')

    if plot_male:
        category = "Male"
        top_male = top_names[top_names['sex'] == 'M'].nlargest(10, 'count')
        sns.barplot(data=top_male, x='count', y='name')

    plt.title(f"Top 10 {category} Names in {year_of_interest}")
    plt.xlabel('Count')
    plt.ylabel('Name')
    plt.tight_layout()
    st.pyplot(fig)