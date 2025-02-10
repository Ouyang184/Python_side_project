# The Analysis

## 1. What are the most demanded skills for the top 3 most popular data roles?

To find the mos demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and go the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills I should pay attention to depending on the role I'm targeting.

View my notebook with detailed steps here: [[2_Skills_count.ipynb]()](Final_Project\2_Skills_count.ipynb)

### Visualize data

```
python
fig, ax = plt.subplots(len(job_titles), 1)

sns.set_theme(style='ticks')
for i, job_title in enumerate(job_titles):
    df_plot = df_skills_count[df_skills_count['job_title_short'] == job_title].head(5)
    # df_plot.plot(kind = 'barh', x ='job_skills', y ='skill_count', ax = ax[i], title = job_title)
    sns.barplot(data= df_plot, x = 'skill_count', y = 'job_skills', ax = ax[i], hue= 'skill_count', palette= 'dark:g_r')
    ax[i].invert_yaxis()
    ax[i].set_ylabel('')
    ax[i].legend().set_visible(False)

fig.suptitle('Counts of Top Skills in Job Posting', fontsize = 15)
plt.tight_layout()
plt.show()
```

### Results

![Visualization of Top Skills for Job Scouting](Final_Project/images/Counts_of_Top_Skills_in_Job_Posting.png)

### Insights

* **SQL dominates across all roles** – It appears as the most in-demand skill for Data Analysts, Data Engineers, and Data Scientists.
* **Python is consistently valuable** – Featured prominently in all three roles, reinforcing its importance in data-related jobs.
* **Excel & Tableau are strong for Data Analysts** – These visualization tools are highly relevant for analysts but less emphasized in other roles.
* **Cloud & Big Data skills for Data Engineers** – AWS, Azure, and Spark are unique to the Data Engineer role, highlighting the focus on cloud infrastructure.
* **R is mainly relevant for Data Scientists** – Unlike Analysts and Engineers, Data Scientists use R more frequently.
* **SAS is still used but less dominant** – Present across roles but not as high as Python and SQL

## 2. How are in-demand skills trending for Data Analysts?

To understand the most in-demand skills for Data Analysts, I first identified the  top three most popular data-related job titles . After filtering the job postings, I extracted the top five most frequently mentioned skills for each of these roles.

### Visualize Data

```
python
sns.lineplot(data = df_plot_trend, palette= 'tab10', legend= False, dashes= False)

sns.despine()
plt.title('Trending Top Skills for Data Analysts in the US')
plt.ylabel('Likelihood in Job Posting')
plt.xlabel('2022')
sns.set_theme(style='ticks')

from matplotlib.ticker import PercentFormatter
ax = plt.gca()
ax.yaxis.set_major_formatter(PercentFormatter(decimals= 0))

for i in range(5):
    plt.text(11.2,df_plot_trend.iloc[-1,i], df_plot_trend.columns[i])
```

### Results

![Trending Top Skills for Data Analysts in the US](Final_Project/images/Trending_Top_skills.png)

### Insights

* **SQL remains the most in-demand skill**
  * Consistently above  **60% likelihood in job postings** , making it a must-have skill for Data Analysts.
  * Slight  **decline in the second half of the year** , but still dominant.
* **Excel demand fluctuates but declines toward year-end**
  * Stable demand in the first half of the year, with a  **spike around mid-year (June-August)** .
  * **Notable drop in Q3** , possibly due to increased preference for more advanced tools.
* **Python shows steady growth**
  * Fluctuates around  **30% throughout the year** , maintaining relevance.
  * **Slight increase in December** , indicating rising demand in job postings.
* **Tableau demand shows a gradual decline**
  * Started the year near  **30%** , but  **dropped toward the second half of the year** .
  * Could indicate a shift towards other BI tools (e.g., Power BI) or automaton tools.

## 3. How well do jobs and skills pay for Data Analysts?

### Salary Analysis for Job Scounting

To understand the salary landscape for Data Analysts, I analyzed compensation trends across various job titles and key skills. This analysis helps identify which roles and skill sets offer the highest earning potential, allowing for more strategic career planning.

### Visualize Data

```
python
sns.boxplot(data = df_us_top6, x = 'salary_year_avg', y = 'job_title_short', order = job_order)

ax = plt.gca()
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'${int(x/1000)}K'))
plt.xlim(0,600000)
plt.title('Salary Distribution in the United States')
plt.xlabel('Yearly Salary ($USD)')
plt.ylabel('')
plt.show()

```

```
python
# # Create a figure with two vertically stacked subplots
fig, ax = plt.subplots(2,1)

# Set the Seaborn theme for better aesthetics
sns.set_theme(style='ticks')

# ------------------- First Bar Plot ------------------- #

# Create a horizontal bar plot for the highest-paid skills for Data Analysts
sns.barplot(data= df_Da_Top_pay, x='median', y = df_Da_Top_pay.index, ax = ax[0], hue = 'median', palette= 'dark:b_r', legend= False)

# Alternative approach (commented out) using Pandas built-in plotting function
# df_Da_Top_pay.plot(kind = 'barh', y = 'median', ax = ax[0], legend= False)

# Set the title for the first subplot
ax[0].set_title('Top 10  Highest Paid Skills for Data Analyst')

# Remove axis labels for a cleaner look
ax[0].set_xlabel('')
ax[0].set_ylabel('')

# Format x-axis labels to display salaries in thousands (e.g., "$50K" instead of "50000")
ax[0].xaxis.set_major_formatter(plt.FuncFormatter(lambda x , pos: f'${int(x/1000)}K'))

# ------------------- Second Bar Plot ------------------- #

# Create a horizontal bar plot for the highest-paid in-demand skills for Data Analysts
sns.barplot(data= df_Da_skills, x='median', y = df_Da_skills.index, ax = ax[1], hue= 'median', palette= 'light:b', legend= False)

# Ensure both subplots share the same x-axis range for better comparison
ax[1].set_xlim(ax[0].get_xlim())

# Set the title for the second subplot
ax[1].set_title('Top 10 Highest Paid Demand Skills')

# Label the x-axis appropriately
ax[1].set_xlabel('Mediean Salary ($USD)')

# Remove the y-axis label for a cleaner look
ax[1].set_ylabel('')

# Format x-axis labels for salary in thousands (same as the first subplot)
ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x , pos: f'${int(x/1000)}K'))


# ------------------- Final Formatting ------------------- #

# Adjust subplot spacing to prevent overlapping titles and labels
fig.tight_layout()
plt.show()

```

### Result

![Salary Distributions of Data Jobs in the US](Final_Project/images/Salary_Distribution_In_US.png)

![The Highest Paid & Most In-Demand Skills for Data Analysts in the US](Final_Project/images/Top_Highest_Paid_Skills.png)Insights

**Senior roles command significantly higher salaries**

* **Senior Data Scientists & Senior Data Engineers** have the highest median salaries, often exceeding  **$150K** .
* **Senior Data Analysts** earn notably more than entry-level Data Analysts, but the gap is smaller than in other roles.

**Data Science & Data Engineering pay more than Data Analysis**

* **Data Scientists and Data Engineers** earn higher median salaries than Data Analysts.
* Their  **upper salary ranges extend past $250K-$300K** , while Data Analysts mostly cap under  **$200K** .

**Significant salary variation & outliers**

* All roles show  **large salary ranges** , with some reaching  **$400K-$500K+** , likely due to high-paying tech companies, FAANG roles, or specialized skills.
* **Outliers are more frequent for Data Scientists & Engineers** , suggesting opportunities for exceptionally high salaries.

**Top 10 Highest Paid Skills for Data Analysts**

* **Programming and DevOps-related skills dominate** the highest-paid category.
* **dplyr** (R package),  **bitbucket** ,  **gitlab** , and **solidity** (blockchain) lead in salary potential, exceeding **$175K** median salary.
* **Hugging Face and Couchbase** , which focus on AI/ML and NoSQL databases, also offer high salaries.
* **Ansible and VMware** indicate a demand for  **automation and cloud infrastructure knowledge** .

**Top 10 Highest Paid Demand Skills**

* **Python remains the highest-paid mainstream skill** , reinforcing its importance in data analysis and engineering.
* **Tableau and Power BI** are highly valued, suggesting continued demand for data visualization.
* **SQL Server and SQL** rank high, confirming that database expertise is key for high-paying roles.
* **Excel, Word, and PowerPoint** appear at the lower end, indicating that while still relevant, they **do not command the highest salaries** compared to technical skills.

**Key Takeaways**

* Specialized programming tools (dplyr, Solidity) and DevOps skills pay more than general data skills.
* Python, SQL, and BI tools remain critical for well-paying jobs.
* Cloud, database, and automation skills (Cassandra, Ansible, VMware) provide strong earning potential.
* While Excel and PowerPoint are useful, they are not associated with the highest salaries.
