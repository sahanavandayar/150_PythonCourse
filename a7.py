from neural import *
#assignment 7

#PART 1

neuralNet = NeuralNet(2, 2, 1)
#this was given below
XORdata = [([0,0], [0]), ([0,1], [1]),([1,0], [1]),([1,1], [0])]
neuralNet.train(XORdata, iters=7000)


#neural net 1
neuralNet1 = NeuralNet(2, 2, 1)
neuralNet1.train(XORdata, iters = 2000, print_interval = 25)
#neural net 2
neuralNet2 = NeuralNet(2, 2, 1)
neuralNet2.train(XORdata, iters = 2000, print_interval = 25)

#PART 2
neuralNet3 = NeuralNet(2, 7, 1)
neuralNet3.train(XORdata, iters = 2000)


#PART 3
neuralNet4 = NeuralNet(2, 7, 1)
neuralNet4.train(XORdata, iters = 2000)


#PART 4
politics = NeuralNet(5,4,1)
opinions = [([0.9,0.6,0.8,0.3,0.1],[1]),
            ([0.8,0.8,0.4,0.6,0.4],[1]),
            ([0.7,0.2,0.4,0.6,0.3],[1]),
            ([0.3,0.1,0.6,0.8,0.8],[0]),
            ([0.6,0.3,0.4,0.3,0.6],[0])]

politics.train(opinions, iters = 450, print_interval = 25)


testOpinions = [[1.0,1.0,1.0,0.1,0.1],
            [0.5,0.2,0.1,0.7,0.7],
            [0.8,0.3,0.3,0.3,0.8],
            [0.8,0.3,0.3,0.8,0.3],
            [0.9,0.8,0.8,0.3,0.6]]

politics.train(opinions, iters = 450, print_interval = 25)

for triple in politics.test(testOpinions):
    print(triple)






