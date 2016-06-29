import sys
from scipy.stats import binom_test

successes = int(sys.argv[1])
trials = int(sys.argv[2])

desired_success_rate = int( sys.argv[ 3 ])/100 if len( sys.argv ) == 4 else 90/100
desired_confidence = int( sys.argv[ 4 ]) if len( sys.argv ) == 5 else 95

p_value_pass = binom_test( successes, trials, desired_success_rate, alternative="greater" )
p_value_fail = binom_test( successes, trials, desired_success_rate, alternative="less" )
result_pass = ( 1 - desired_confidence / 100 ) > p_value_pass
result_fail = ( 1 - desired_confidence / 100 ) > p_value_fail
print( result_pass )
print( result_fail )

print( "\ndesired confidence is: {0}".format( desired_confidence ) )
print( "p value for success is: %f" % p_value_pass )
print( "p value for failure is: %f" % p_value_fail )

print( "\nWhat’s the result?" )

if result_pass:
    print( "They passed the test! We can be confident that they meet the desired accuracy rate." )
elif result_fail:
    print( "They failed the test! We can be confident that they don’t meet the desired accuracy rate." )
else:
    print( "Need more trials..." )
