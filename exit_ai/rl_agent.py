# exit_ai

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class PolicyNetwork(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(PolicyNetwork, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim, 128),
            nn.ReLU(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1),
        )

    def forward(self, x):
        return self.fc(x)

class PPOAgent:
    def __init__(self, state_dim, action_dim, lr=3e-4, gamma=0.99, eps_clip=0.2):
        self.policy = PolicyNetwork(state_dim, action_dim)
        self.optimizer = optim.Adam(self.policy.parameters(), lr=lr)
        self.gamma = gamma
        self.eps_clip = eps_clip

    def select_action(self, state):
        probs = self.policy(torch.tensor(state, dtype=torch.float))
        dist = torch.distributions.Categorical(probs)
        action = dist.sample()
        return action.item(), dist.log_prob(action)

    def update(self, states, actions, rewards, log_probs_old):
        discounted_rewards = []
        R = 0
        for r in reversed(rewards):
            R = r + self.gamma * R
            discounted_rewards.insert(0, R)
        discounted_rewards = torch.tensor(discounted_rewards, dtype=torch.float)

        new_log_probs = []
        for state, action in zip(states, actions):
            probs = self.policy(torch.tensor(state, dtype=torch.float))
            dist = torch.distributions.Categorical(probs)
            new_log_probs.append(dist.log_prob(torch.tensor(action)))

        ratios = torch.exp(torch.stack(new_log_probs) - torch.stack(log_probs_old))
        advantages = discounted_rewards - discounted_rewards.mean()
        loss = -torch.min(
            ratios * advantages,
            torch.clamp(ratios, 1 - self.eps_clip, 1 + self.eps_clip) * advantages,
        ).mean()

        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
