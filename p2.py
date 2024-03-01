inputs=[1,2,3,4] 
weights=[[1.3,2.4,-2.3,1.2],[3.0,-2.0,1.0,0.5],[2.5,-0.6,-0.1,5.0]] # now each row represents weights towards that neuron, 3 neurons are being considered here
bias=[2,2,2] #the value of bias is actually the value of a neuron, here there are 3 values because 3 neurons are being considered 


output=[inputs[0]*weights[0][0]+inputs[1]*weights[0][1]+inputs[2]*weights[0][2]+inputs[3]*weights[0][3]+bias[0],
        inputs[0]*weights[1][0]+inputs[1]*weights[1][1]+inputs[2]*weights[1][2]+inputs[3]*weights[1][3]+bias[1],
        inputs[0]*weights[2][0]+inputs[1]*weights[2][1]+inputs[2]*weights[2][2]+inputs[3]*weights[2][3]+bias[2]]
print(output)