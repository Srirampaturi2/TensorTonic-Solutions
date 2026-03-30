import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    
    """
     Write code here. Updates itself with the Experience policy over episodes
    get Rewards, states from Time window Episodes -> Calc Backwards returns -> cal V (       sum/count )

    Ep1: Robot tries to pick cup → drops it ❌
    Ep2: Robot tries to pick cup → succeeds ✅
    Ep3: Robot tries to pick cup → succeeds ✅
    
    S0 = "cup is 30cm away"
    S1 = "hand is 10cm from cup"
    S2 = "fingers touching cup"
    S3 = "cup grasped successfully"
    
    r = -1  → wasted movement (penalize)
    r = 0   → neutral action
    r = +10 → successfully grabbed cup! (reward)

    Robot at S1 (hand near cup):
G = r1 + 0.9*r2 + 0.9²*r3
  = 0  + 0.9*0  + 0.81*10 = 8.1
------  V(s) -- How good it is to be at this state 
   V(S0) = 7.2  → being far from cup is ok but not great
   V(S1) = 8.1  → being near cup is better!
   V(S2) = 9.0  → touching cup is even better!
   V(S3) = 10.0 → grasping cup = best state! 🎯
    
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)
    for e in episodes:
        visited =set()
        G=0
        for t in range(len(e)-1,-1,-1):
          state, reward = e[t]
          G = reward+ gamma * G   # Use reward and Cal G retuens r3 + g*0 =G -> r2 + g(r3)  -> r1 + g*r2+g2*r3)= G 
           #if state not in visited:   # Use state for 1 visit
          returns_sum[state] = G
          returns_count[state] = 1
          visited.add(state)
    V = np.divide(returns_sum, returns_count, out=np.zeros(n_states), where=returns_count!=0)
    return V
    """
    returns_sum = np.zeros(n_states)
    returns_count = np.zeros(n_states)
    
    for e in episodes:
        first_visit = {}
        G = 0
        for t in range(len(e)-1, -1, -1):
            state, reward = e[t]
            G = reward + gamma * G
            first_visit[state] = G  # overwrite within episode
        
        for state, g in first_visit.items():
            returns_sum[state] += g      # add across episodes
            returns_count[state] += 1
    
    V = np.divide(returns_sum, returns_count, out=np.zeros(n_states), where=returns_count!=0)
    return V
    
   
        
        