# Cooldown for Artifact Investigation is 180s from rank N to B, 120s from rank A to 8, 60s from 7 to 4, and 30s from 3 to 1
# could also use open-cv to determine when Artifact Investigation is off cooldown, but seems a bit more intensive

# click on skill
# window opens prompting to select an item
# select item via leftclick
# left click ok
# yet another window prompt asking to confim
# left click ok
# wait for number of sec depending on skill rank
# this process is the same for both artifact appraisal and restoration, with slightly different window prompts

def determineCD(rank):
    match rank:
        case '1' | '2' | '3' :
            return 30
        case '4' | '5' | '6' | '7':
            return 60
        case '8' | '9' | 'A':
            return 120
        case default:
            return 180