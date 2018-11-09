# Game Theory Cheetsheet

**Game theory** is the study of mathematical models of conflict and cooperation between intelligent rational decision-makers. Game theory is mainly used in economics, political science, and psychology, as well as logic, computer science and biology.

## Basic concepts

**Players / Agents**: who?

**Actions**: what to do?
- Enter a bid in an auction? Decide whether to end a strike? Decide when to sell a stock? Decide how to vote?...

**Payoffs**: how much?
- Do they care about some profit? Do they care about other players?...

### Normal form 

- Lists what payoffs players get as a function of their actions. 
- Does not incorporate any notion of sequence, or time, of the actions of the players.
- Usually represented by a matrix.

#### Normal form representing Prisoner's Dilemma
|                 | **Stay silent**       | **Betray**          |
| ---             | ---                   | ---                 |
| **Stay silent** | -1,-1                 | -3,0                |
| **Betray**      | 0,-3                  | **-2,-2**           |

* __Simultaneous games__ (a.k.a. Strategy games) : games where both players move simultaneously, or if they do not move simultaneously, the later players are unaware of the earlier players' actions (making them effectively simultaneous).
* __Sequential games__: games where later players have some knowledge about earlierr actions.
* __Perfect information games__: games in which all players know the moves previously made by all other players.
* __Complete information games__: games in which all players know the strategies and payoffs available to the other players.


## Terminologies
* __coordination game__: multiple pure strategy Nash equilibria in which players choose the same or corresponding strategies.

* __Nash equilibrium__: a proposed solution of a non-cooperative game involving two or more players in which each player is assumed to know the equilibrium strategies of the other players, and no player has anything to gain by changing only their own strategy
