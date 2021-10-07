# HighWaterMark
High water marks are used to compute the performance fees paid to a hedge fund by its investors. When I was interning at an investment company, I was asked to look into the situation in which a hedge fund falls so far under its high water mark (as happened in 2008-2009) that its managers have little chance of earning a performance fee for several years to come. The investment company was interested in restructuring their contracts with the hedge funds in which they invested which found themselves in this situation. (I believe they had already done this when I worked there in 2013, but was planning for future crashes)

At the investment company I used a Monte Carlo type simulation with randomly sampled past returns to simulate future outcomes. I could then simulate each renegotiated contract many times and compare statistics on the outcomes. This used nonpublic data however.

Filinggrabber pulls 13Fs from the SEC website for a particular list of hedge funds. These are filings in which large hedge funds must report their long holdings. Using this, I can try to make a proxy for past returns. 


