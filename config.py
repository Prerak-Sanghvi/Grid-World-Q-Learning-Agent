ENV_CONFIG = {
    "size": (10, 10),
    "start": (0, 0),
    "goal": (9, 9),
    "obstacles": [
        (1, 3), (2, 3), (3, 3), (4, 3),
        (6, 1), (6, 2), (6, 3), (6, 4),
        (7, 7), (8, 7), (9, 7), (2, 8),
        (1, 9), (2, 9)
    ]
}

AGENT_CONFIG = {
    "alpha": 0.1,
    "gamma": 0.99,
    "epsilon": 1.0,
    "epsilon_decay": 0.995,
    "min_epsilon": 0.01
}
