'''@file evaluator_factory.py
contains the Evaluator factory'''

from . import  decoder_evaluator

def factory(evaluator):
    '''
    gets an evaluator class

    Args:
        evaluator: the evaluator type

    Returns:
        an evaluator class
    '''

    if evaluator == 'decoder_evaluator':
        return decoder_evaluator.DecoderEvaluator
    else:
        raise Exception('Undefined evaluator type: %s' % evaluator)
