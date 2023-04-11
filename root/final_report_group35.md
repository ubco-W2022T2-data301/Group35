# Introduction 

There are many important things that is required to know before investing in stocks, this is informed in detail in the final report of the project. 

To start, Saketh was interested in how the visializations and analysis of datasets can be used to smartly invest in stocks without any risk of loss and more probability to maximize the returns and profits. This is a very important and useful information to always know as it primarily saves our money, especially during the infaltion and all the taxes. Suppose upon analysing 7 companies interested to invest in, there are 3 companies that show maximum return and success, then instead of fully investing in 1 place, it can be split and invested in 3 places so that it further reduces the risk of any loss.  

Likewise, Vanshika was interested to explore more about the Exchange Traded Funds  Models as they are an important investment option due to their low-cost diversification, high liquidity, transparency, and flexibility in investment strategies. Further, they offer investors an efficient way to gain diversified exposure to a wide range of asset classes, while also being able to trade quickly and efficiently throughout the day, it adds more value in our project. The transparency of ETFs allows investors to make informed decisions about which ETFs to invest in and monitor their performance over time. ETFs also offer flexibility in terms of investment strategies, allowing investors to tailor their portfolios to their specific investment goals and risk tolerance. As such, ETFs have become an increasingly popular investment option for both individual and institutional investors. Due to these important factors, she analysis the data of all the tech industries and make the ETF baskets for the Yearly and Monthly basis.

And finally, Shakthi did research and analysis in the stock market to find ideal companies for investors to invest in. After analyzing the data, it was found that the companies that are most profitable and less volatile are Apple, Tesla, Amazon, Meta, and Microsoft. A factor called "Market Value" was created by using different attributes of each individual company, and this was used to find the companies mentioned. Market Value is calculated by finding the product of average stock price and the volume of stocks sold. This value is then divided by 10^8 to scale down the market value to a 0-100 range. It was also found out that certain companies had a high volume of stock volume, but the average stock price was low. However, they had a high market value because of the high volume of stocks sold. This was found to be the case for companies like Tesla, Amazon, and Apple. These companies were found to be the most profitable and less volatile.



### Analysis 1 (Vanshika)

### Which Technology based industries are secure to be included in an Yearly and a Monthly ETF model?

Initially, I observed that there are significantly more tech companies in the data frame than companies from other fields, which may skew the results. Despite this minority, I recognize that tech companies have a positive return on investment, 
so I will focus exclusively on the tech industry to ensure more accurate results. This ETF will provide investors with positive returns and fewer fluctuations. 
### Monthly ETF
![Monthly Profit](images/Screenshot%202023-04-10%20201927.png)
Clearly, AMD, SALESFORCE , Nvidia and Yelp are not profitable so we can skip these companyies for our Monthly EFT Basket.

Let's take a look at the  standard deviation of the close value of these stocks as the measure of the volatility of the asset's returns over the chosen time period. The higher the standard deviation, the greater the volatility
![Monthly Volatility](images/A1a.png)
Meta, Nvidia and Salesforce are showing the most Volatility on monthly basis. 

CONCLUSION FOR MONTHLY ETF BASKET-
![](https://tse4.mm.bing.net/th?id=OIP.0IkVQ7FUR0vFqbYE-PNYFgHaE8&pid=Api&P=0)
After looking at all the graphs and relationS. The favourable companies that are more profitable and less Volatile will be

- Microsoft
- Intel
- Google
- Apple
- Cisco


### For the Yearly ETF

![Alt text](images/Screenshot%202023-04-10%20201950.png)

We observe that certain companies show considerably high volatility in their stock prices. Specifically, AMD, Nvidia, and Yelp have been identified as highly volatile companies that may not be suitable for the EFT if their profits are not good enough.

On the other hand, companies like 
![](https://tse4.mm.bing.net/th?id=OIP.UmM-ZlsC_G3p6usKR95i0QHaEK&pid=Api&P=0)
- Microsoft
- Meta
- Intel
- Google
- Cisco
- Apple

have shown positive values in their profit and are less volatile. Therefore, based on our analysis, we can conclude that these companies would be suitable for our yearly Bucket.

### Analysis 2 summary (Saketh)
Question - How proper analysis of the data can help in making informed decisions on which company to invest in stocks

I had come with an idea to do excatly that, how I did this was calculating the profit value of all the companies and conpare them and see which has the biggest profit returns. Knowing this, we can invest there to reduce the risk of any loss.
I had calculated the profit of each company by - Profit = Volume per Company * Closing value per Company
We can see exactly that over here:
![Profit of the top 5 companies among the 30](images/pic1.png)

Along with this I had also realised that analysing the volume of shares sold per company can also be informative as that shows how succesful the companies are so I had made a graph to excatly show that:
![Volumes sold of the top 5 companies among the 30](images/pic2.png)

With that it is easy to conclude that Apple, Amazon and Tesla are the best to invest in among the 30 companies as they have the highest volume of shares sold as well as the highest returns of profit.
I personally would split my investments among these 3 companies so that it would thrive and maximise my returns and prevent any loss.

[Further analysis can be seen in my analysis notebook over here including code and the data](../analysis/analysis2.ipynb)







