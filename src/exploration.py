import creation
import communication
import matplotlib.pyplot as plt

path = '/Users/maxwiese/Documents/DSI/assignments/Research-Funding-CMS/data/'\
    'Research_Payment_Data___Detailed_Dataset_2019_Reporting_Year.csv'

df_2019 = creation.cleaning(path)

# Build visualization for Funding Areas
fig0, ax0 = plt.subplots(3, figsize = (16,8))

# Total
communication.one_dim_scatterplot(
    df_2019.Total_Amount_of_Payment_USDollars.values,
    ax0[0], alpha=0.5, color='b', s = 25)
ax0[0].scatter(
    df_2019.Total_Amount_of_Payment_USDollars.mean(),
    0, color='red', s=100)

# Products
communication.one_dim_scatterplot(
    df_2019[df_2019.Related_Product_Indicator == 'Yes']
    .Total_Amount_of_Payment_USDollars.values,
    ax0[1], alpha=0.5, color='b', s = 25)
ax0[1].scatter(
    df_2019[df_2019.Related_Product_Indicator == 'Yes']
    .Total_Amount_of_Payment_USDollars.mean(), 0, color='red',
    s=100)

# Not Products
communication.one_dim_scatterplot(
    df_2019[df_2019.Related_Product_Indicator == 'No']
    .Total_Amount_of_Payment_USDollars.values,
    ax0[2], alpha=0.5, color='b', s = 25)
ax0[2].scatter(
    df_2019[df_2019.Related_Product_Indicator == 'No']
    .Total_Amount_of_Payment_USDollars.mean(), 0, color='red',
    s=100)

fig0.suptitle('Distribution of Funding Amount Per Relationship', fontsize=16)
ax0[0].set_title('All Payments 2019')
ax0[1].set_title('Product Payments 2019')
ax0[2].set_title('Non-Product Payments 2019')
ax0[0].set_xlabel('Funding (10 Millions USD)')
ax0[1].set_xlabel('Funding (10 Millions USD)')
ax0[2].set_xlabel('Funding (10 Millions USD)')
fig0.tight_layout()
plt.show()

# Build visualization funding by product type
fig1, ax1 = plt.subplots(3, figsize = (16,8))

# Drug Related Products
communication.one_dim_scatterplot(
    df_2019[df_2019.Drug_Related == True]
    .Total_Amount_of_Payment_USDollars.values,
    ax1[0], alpha=0.5, color='b', s = 25)
ax1[0].scatter(df_2019[df_2019.Drug_Related == True]
    .Total_Amount_of_Payment_USDollars.mean(), 0, color='red', s=100)

# Biological Related Products
communication.one_dim_scatterplot(
    df_2019[df_2019.Biological_Related == True]
    .Total_Amount_of_Payment_USDollars.values,
    ax1[1], alpha=0.5, color='b', s = 25)
ax1[1].scatter(df_2019[df_2019.Biological_Related == True]
    .Total_Amount_of_Payment_USDollars.mean(), 0, color='red', s=100)

# Medical Device Related Products
communication.one_dim_scatterplot(
    df_2019[df_2019.Device_Related == True]
    .Total_Amount_of_Payment_USDollars.values,
    ax1[2], alpha=0.5, color='b', s = 25)
ax1[2].scatter(df_2019[df_2019.Device_Related == True]
    .Total_Amount_of_Payment_USDollars.mean(), 0, color='red', s=100)

fig1.suptitle(
    'Distribution of Funding Amount Per Relationship By Product Type',
    fontsize=16)
ax1[0].set_title('Drug Related Product Payments 2019')
ax1[1].set_title('Biological Related Product Payments 2019')
ax1[2].set_title('Medical Device Related Product Payments 2019')
ax1[0].set_xlabel('Funding (10 Millions USD)')
ax1[1].set_xlabel('Funding (10 Millions USD)')
ax1[2].set_xlabel('Funding (Millions USD)')
fig1.tight_layout()
plt.show()

# Build a visualization for depencies within product related funding
fig2, ax2 = plt.subplots(figsize=(8, 12))
communication.stacked_bars(df_2019, ax2)

# Calculate statistical significance 
v1, v2, t, p = creation.stats_of_interest(
    df_2019[df_2019.Drug_Related == True]
    .Total_Amount_of_Payment_USDollars.values,
    df_2019[df_2019.Related_Product_Indicator == 'No']
    .Total_Amount_of_Payment_USDollars.values)

print("Variance of Drug Related Funding is {:.2f}".format(v1))
print("Variance of Nonproduct Related Funding is {:.2f}".format(v2))
print("t Score is {:.2f}".format(t))
print("p value is {:.2e}".format(p))
