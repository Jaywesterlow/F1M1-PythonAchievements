import math


trees               = 333
shadedTrees         = trees / 3 * 2
sunnyTrees          = trees / 3

shadeOutputModifier = 80

sunnyTreeOutput     = 146
shadedTreeOutput    = sunnyTreeOutput /100 * shadeOutputModifier

sunnyOutput         = sunnyTrees * sunnyTreeOutput
shadedOutput        = shadedTrees * shadedTreeOutput
totalOutput         = sunnyOutput + shadedOutput

owners              = 3

sellableOutput      = math.floor(totalOutput)
eatCount            = totalOutput - sellableOutput 
cut                 = sellableOutput / owners

print(cut)