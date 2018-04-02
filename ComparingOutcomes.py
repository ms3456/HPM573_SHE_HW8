import Parameters as P
import Classes as Cls
import SupportSteadyState as SupportSteady
import SupportTransientState as SupportTransient

print ('Problem 1 Comparing outcomes in a steady-state scenario')
# create a set of game with a fair coin (probablity of head is 0.5) for a STEADY state
SteadyFair=Cls.SetOfGames(id=1, prob_head=P.PROB_HEAD_FAIR, n_games=P.N_GAMES)
# simulate the set
SteadyFairOutcomes=SteadyFair.simulation()


#create a set of game with an unfair coin (probability of head is 0.45) for a STEADY state
SteadyUnfair=Cls.SetOfGames(id=1, prob_head=P.PROB_HEAD_UNFAIR, n_games=P.N_GAMES)
#simulate the set
SteadyUnfairOutcomes=SteadyUnfair.simulation()

# get change in reward for the steady state
SupportSteady.print_outcomes(SteadyFairOutcomes, "When the probability of head is 0.5")
SupportSteady.print_outcomes(SteadyUnfairOutcomes, "When the probability of head is 0.45")
SupportSteady.print_comparative_outcomes(SteadyFairOutcomes, SteadyUnfairOutcomes)


print()
print('Problem 2 Comparing outcomes in a transient-state scenario')
# create multiple sets of games with a fair coin for a TRANSIENT state
multiGameSetsFair=Cls.MultipleGameSets(ids=range(P.NUM_SIM_GAMESETS), prob_head=P.PROB_HEAD_FAIR, n_games_in_a_set=P.REAL_GAME_SET)
#simulate
TransientFairOutcomes=multiGameSetsFair.simulation()


#create a set of game with an unfair coin (probability of head is 0.45) for a TRANSIENT state
multiGameSetUnfair=Cls.MultipleGameSets(ids=range(P.NUM_SIM_GAMESETS), prob_head=P.PROB_HEAD_UNFAIR, n_games_in_a_set=P.REAL_GAME_SET)
#simulate the set
TransientUnfairOutcomes=multiGameSetUnfair.simulation()

# get the change in reward for a transient state
SupportTransient.print_outcomes(multiGameSetsFair, 'When the probability of head is 0.5')
SupportTransient.print_outcomes(multiGameSetUnfair, "When the probability of head is 0.45")
SupportTransient.print_comparative_outcomes(multiGameSetsFair, multiGameSetUnfair)