import gymnasium as gym

env = gym.make('FrozenLake-v1', render_mode ='human')

## Obtener info del entorno
print("Numero de estados:", env.observation_space.n)
print("Numero de acciones:", env.action_space.n)
