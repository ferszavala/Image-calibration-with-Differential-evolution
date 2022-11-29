import numpy as np

class DE:
    def __init__(self, objfunc, bounds, args=(), popsize=10,plotFunction=None,childSelectionRate=0.9, recombinationRate=0.8):
        self.objfunc = objfunc
        self.args = args
        self.bounds = bounds
        self.boundsSize = len(bounds)
        self.population = None
        self.popsize = popsize
        self.fitness = None
        self.plotFunction = plotFunction
        self.iteration = 0
        self.childSelectionRate=childSelectionRate
        self.recombinationRate=recombinationRate

    def mutation(self):
        x1, x2, x3 = np.random.randint(
            0.1, self.popsize, (3, self.popsize))
        f = np.random.uniform(0, 2, self.popsize)
        self.population[self.popsize:] = self.population[x1] + \
            f[:, None] * (self.population[x2] - self.population[x3])
        for i in range(self.boundsSize):
            self.population[self.popsize:, i] = np.clip(
                self.population[self.popsize:, i], self.bounds[i, 0], self.bounds[i, 1])

    def recombination(self):        
        index = np.random.choice(a=[True, False], size=(self.popsize,self.boundsSize), p=[self.recombinationRate, 1-self.recombinationRate])        
        self.population[self.popsize:, :] = np.where(index, self.population[self.popsize:, :], self.population[:self.popsize, :])

    def selection(self):
        index = np.random.choice(a=[True, False], size=(self.popsize), p=[self.childSelectionRate, 1-self.childSelectionRate])
        index2 = np.invert(index)
        self.fitness[self.popsize:][index] =  np.apply_along_axis(self.objfunc, 1, self.population[self.popsize:][index], *self.args)
       
        self.fitness[self.popsize:][index2] =  self.fitness[:self.popsize][index2]
        self.population[self.popsize:][index2] =  self.population[:self.popsize][index2]        
        orden = self.fitness.argsort()       
        self.fitness = self.fitness[orden]
        self.population = self.population[orden]

    def initializePopulation(self):
        self.iteration = 0
        self.population = np.ones((self.popsize*2, self.boundsSize))
        self.fitness = np.zeros(self.popsize*2)
        for i in range(self.boundsSize):
            self.population[:, i] = np.random.uniform(
                self.bounds[i, 0], self.bounds[i, 1], (self.popsize*2))
        self.population[:, i] = np.clip(
            self.population[:, i], self.bounds[i, 0], self.bounds[i, 1])
        self.fitness = np.apply_along_axis(self.objfunc, 1, self.population, *self.args)

    def solve(self, continueTraining=False, maxIterations=1000, stopValue=0, earlyTerminationMaxIterations=np.inf, earlyTerminationTolerance=0.01):
       
        if not continueTraining:
            self.initializePopulation()
            
        for i in range(maxIterations):
            self.iteration += 1
            self.mutation()
            self.recombination()
            self.selection()
            if self.plotFunction is not None:
                self.plotFunction(self.population[0, :len(self.bounds)],*self.args)
            print ({"It": self.iteration, "Vals": self.population[0, :len(self.bounds)], "Fit": self.fitness[0]})

        return {"It": self.iteration, "Vals": self.population[0, :len(self.bounds)], "Fit": self.fitness[0]}

def differential_evolution(objfunc, bounds, args=(), popsize=10, plotFunction=None,childSelectionRate=0.9, recombinationRate=0.8):
    de = DE(objfunc, bounds, args, popsize=10, plotFunction=plotFunction,childSelectionRate=0.9, recombinationRate=0.8)
    return de.solve(maxIterations=2000)