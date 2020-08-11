import matplotlib.pyplot as plt
from random import random,randint
import numpy as np
from collections import defaultdict

vector = np.array([(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0)])

class Cell(object):

  def __init__(self,leq60):
    if leq60:
      self.gamma = gamma_leq60
      self.lambda_ = lambda_leq60
      self.t = t_leq60
      self.a = a_leq60
    else:
      self.gamma = gamma_geq60
      self.lambda_ = lambda_geq60
      self.t = t_geq60
      self.a = a_geq60
    self.state = "Infected" if random() < alpha else "Suspicious"
    self.pos = np.array((int(random()*BOUNDARY),int(random()*BOUNDARY)))
    self.time = 0

  def move(self):
    if (self.state == "Infected" and random() < self.a*self.lambda_) or (self.state in ["Suspicious","Recovered"] and random() < self.lambda_):
      v = vector[randint(0,7)] 
      if 0 <= self.pos[0] + v[0] <= BOUNDARAY and 0 <= self.pos[1] + v[1] <= BOUNDARY:
        self.pos += v

  def infect(self):
    if random() < alpha and self.state == "Suspicious":
      self.state = "Infected"

  def update(self,infected_num):
    if self.state == "Infected":
      if infected_num >= N:
        p = random()
        if p < beta_dash:
          self.state = "Recovering"
        elif p > 1 - self.gamma:
          self.state = "Dead"
      else:
        if random() < beta:
          self.state = "Recovering"
    elif self.state == "Recovering":
      self.time += 1
      if self.time >= self.t:
        self.state = "Suspicious"
        self.time = 0

class Simulator:
  def __init__(self):
    self.cells = [Cell(True) for _ in range(N_leq60)] + [Cell(False) for _ in range(N_geq60)]
    self.state_leq60 = np.array([])
    self.state_geq60 = np.array([])
  
  def simulate(self):

    for _ in range(TIME):
      infected_num = sum([cell.state == "Infected" for cell in self.cells])
      num_leq60 = defaultdict(list)
      num_geq60 = defaultdict(list)

      for s in ["Suspicious","Infected","Recovering","Dead"]:
        num_leq60[s] = 0
        num_geq60[s] = 0
      
      for cell in self.cells:
        cell.update(infected_num)
      
      for cell in self.cells[:N_leq60]:
        num_leq60[cell.state] += 1
      
      for cell in self.cells[N_leq60:]:
        num_geq60[cell.state] += 1
      
      if _ == 0:
        print(num_leq60)
      
      self.state_leq60 = np.append(self.state_leq60,np.array(list(num_leq60.values())))
      self.state_geq60 = np.append(self.state_geq60,np.array(list(num_geq60.values())))
      
  
  def show(self):
    t = np.linspace(1,TIME,TIME)

    self.state_leq60 = self.state_leq60.reshape((TIME,4))
    plt.figure(figsize=(15,8))
    plt.fill_between(t,100,label="Suspicious",color="palegreen")
    plt.fill_between(t,100/N_leq60*(self.state_leq60[:,3]+self.state_leq60[:,1]+self.state_leq60[:,2]),label="Recovering",color="skyblue")
    plt.fill_between(t,100/N_leq60*(self.state_leq60[:,3]+self.state_leq60[:,1]),label="Infected",color="tomato")
    plt.fill_between(t,100/N_leq60*self.state_leq60[:,3],label="Dead",color="gray")
    plt.title("Aged <= 60")
    plt.xlabel("time")
    plt.ylabel("rate[%]")
    plt.legend()
    plt.show()

    self.state_geq60 = self.state_geq60.reshape((TIME,4))
    plt.figure(figsize=(15,8))
    plt.fill_between(t,100,label="Suspicious",color="palegreen")
    plt.fill_between(t,100/N_geq60*(self.state_geq60[:,3]+self.state_geq60[:,1]+self.state_geq60[:,2]),label="Recovering",color="skyblue")
    plt.fill_between(t,100/N_geq60*(self.state_geq60[:,3]+self.state_geq60[:,1]),label="Infected",color="tomato")
    plt.fill_between(t,100/N_geq60*self.state_geq60[:,3],label="Dead",color="gray")
    plt.title("Aged >= 60")
    plt.xlabel("time")
    plt.ylabel("rate[%]")
    plt.legend()
    plt.show()

#@title Initial Condition
TIME = 200#@param {type:"number"}
BOUNDARY = 200#@param {type:"number"}
N_leq60 = 200#@param {type:"number"}
N_geq60 = 200#@param {type:"number"}
N = 200#@param {type:"number"}
alpha= 0.9#@param {type:"number"}
beta = 0.02#@param {type:"number"}
beta_dash = 0.005#@param {type:"number"}
gamma_leq60 = 0.001#@param {type:"number"}
gamma_geq60 = 0.005#@param {type:"number"}
t_leq60 = 100#@param {type:"number"}
t_geq60 = 150#@param {type:"number"}
lambda_leq60 = 0.1#@param {type:"number"}
lambda_geq60 = 0.05#@param {type:"number"}
a_leq60 = 0.5#@param {type:"number"}
a_geq60 = 0.3#@param {type:"number"}


sim = Simulator()
sim.simulate()
sim.show()