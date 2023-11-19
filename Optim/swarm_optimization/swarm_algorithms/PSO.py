import numpy as np

class Particle:
    def __init__(self, objective_function, dimension, blo, bup):
        self.position = np.random.uniform(blo, bup, dimension)
        self.velocity = np.random.uniform(-abs(bup - blo), abs(bup - blo), dimension)
        self.best_position = self.position
        self.best_fitness = objective_function(self.position)

def pso_algorithm(objective_function, dimension, num_particles=20, max_generations=1000, inertia_weight=0.5, cognitive_weight=1.5, social_weight=1.5, blo=0, bup=1, opt = None, err = None):
    '''
        Particle swarm optimization - optimizing objective_funtion in a dim dimensional space on a hipercube given by blo and bup boundaries using given particle through given iteration with given parameters
    '''

    # Initialize particles
    particles = [Particle(objective_function, dimension, blo, bup) for _ in range(num_particles)]

    # Initialize global best
    global_best_fitness = min([p.best_fitness for p in particles])
    global_best_position = [p.best_position for p in particles if p.best_fitness == global_best_fitness]
    global_best_position = global_best_position[0]
    
    # Running algorithm for max iterations
    for generation in range(max_generations):

        # Benchmarking options
        if opt != None and abs(global_best_fitness-opt)<err:
            return generation, global_best_fitness

        for particle in particles:
            # Update particle velocity
            rp, rg = np.random.rand(dimension), np.random.rand(dimension)
            particle.velocity = (inertia_weight * particle.velocity +
                                 cognitive_weight * rp * (particle.best_position - particle.position) +
                                 social_weight * rg * (global_best_position - particle.position))
           
            # Update particle position
            particle.position = particle.position + particle.velocity
            #particle.position += particle.velocity
            
            # Enforce linear boundaries
            particle.position = np.clip(particle.position, blo, bup)
            
            # Evaluate fitness
            fitness = objective_function(particle.position)

            # Update personal best
            if fitness < particle.best_fitness:
                particle.best_position = particle.position
                particle.best_fitness = fitness

            # Update global best
            if fitness < global_best_fitness:
                global_best_position = particle.position
                global_best_fitness = fitness
        #print(f"Generation {generation + 1}/{max_generations}: Global Best Fitness = {global_best_fitness}")
        
    if opt != None:
        return generation, global_best_fitness
    return global_best_position, global_best_fitness