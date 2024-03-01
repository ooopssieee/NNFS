inputs=[1,2,3,4] 
weights=[1.3,2.4,-2.3,1.2] # weights on the paths of each input neuron to this neuron
bias=2 #The value of the neuron 


output=inputs[0]*weights[0]+inputs[1]*weights[1]+inputs[2]*weights[2]+inputs[3]*weights[3]+bias
print(output)


#Visual Representation:
#in |hidden |out
#    layers
#   O   O   
#O  O   O   O
#O  O   O   O   
#O  O   O   O
#O  O   O   O
#   O   O   