# Football-Model
Create a model that will generate realistic looking results of a Football League Table, utilising statistical analysis of a sample of Leagues from within UEFA; these being: Premier League, Bundesliga, Serie A, Erevidise, EFL Championship. The League Table data was scrapped from Wikipedia and then collated into the csv file 'All Leagues Final.csv'


## Points per Game and Match Outcome Analysis

Within the 'PPG Anaylsis.py' file, the code outputs two different types of information, utilising the 'All Leagues Final.csv' file. The first is an analysis of the Points per Game statistics, which shows that the PPG distribution is roughly normal but is also slightly positive skewed. It also outputs three key sample statisitcs that lead to this distribution: mean (1.372), median (1.294), and standard deviation (0.442). Then there is the analysis of the Match Outcomes across the leagues, showing the relative distributions for each result of: Win%, Draw%, and Loss%. It also aswell outputs the numerical same numerical statisitics in PPG. Using all of this information, it will help with the creation of a model that generates realisitic looking results of both matches and of a football league table.

The next way to further deepen this analysis would be through seeing how these results change between Leagues, level of competition, and years. This then allowing for a more complex understanding of how PPG and match outcomes could be more realisticaly modeled

## Points per Game and its correlation with other statistics

The 'PPG Correlations.py' file analyises how Points per Game correlates with other statistics, and if there is any causation between statistics.
