import genomics.matching as matching

def test_matchScore_simple():
    '''
    Testing basic behaviour of matchScore
    '''
    score = matching.matchScore('AAA','AAA')
    assert score == 3, 'AAA and AAA should have scored 3, but got %i' % score

def test_penalties():
    '''
    check mis-match behaviour
    '''
    score = matching.matchScore('AAA','CCC')
    assert score == -3, 'AAA and CCC should have scored -3, but got %i' % score

def test_gaps():
    '''
    check gap behaviour
    '''
    score = matching.matchScore('---','---')
    assert score == 0, '--- and --- should have scored 0, but got %i' % score

def test_matchScore_hard():
    '''
    Testing more difficult behaviour of matchScore
    '''
    score = matching.matchScore('GT-CA-','GT-CCA')
    assert score == 2, 'GT-CA- and GT-CCA should have scored 2, but got %i' % score
