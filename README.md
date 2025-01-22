# Dice Average Roll Problem
**The Problem**<br>
A problem from [_A Collection of Dice Problems_](https://www.madandmoonly.com/doctormatt/mathematics/dice1.pdf "A Collection of Dice Problems") by Matthew M. Conroy<br><br>
You roll a single die. You can roll it as many times as you like (or maybe we put an upper bound, like
10 or 100). When you stop, you will recieve a prize proportional to your average roll. When should
you stop? (Experiments indicate it is when your average is greater than about 3.8.)<br><br>
For this solution, the upper bound is set to 50. However it doesn't really impact the end result.
<br><br>
**Proposed Solution**<br>
Calculate the expected new EV average as: $$Expected\ New\ EV\ Average = \frac{Sum\ of\ Rolls\ so\ Far + E[New Roll]}{Number\ of\ Rolls\ so\ Far + 1}$$<br>
Then, stop rolling the die whenever your current average is higher than the expected new average.
<br><br>
**Simulation**<br>
The code does a simulation of 10.000 games and follows the above mentioned rules. The results are as follows:<br>
![alt text](https://github.com/vlunic00/Dice-EV-Game/blob/main/Simulation.png "Simulated Results Graph")<br>
With the following rulset, the lowest threshlod at which you stop rolling is consistantly 5.0. However, following it, you win only ~37% of the time.<br>
Also, the rulset is practically useless if you progress after the second roll, as in the 10.000 simulated games (and over many code executions), if you rolled
more than 2 times, you end up rolling the maximum 50 allowed rolls every time.<br><br>
Therefore, while the solution does yield a high payout, it's dependent almost exclusively on rolling a 6 in your first 2 rolls, meaning it isn't a very robust strategy to follow.
