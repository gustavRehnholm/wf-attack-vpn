def printProgressBar (progress, progressLen, prefix = '', suffix = '', barLen = 50, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    Args:
        progress    - Required  : current progress          (Int)
        progressLen - Required  : total iterations          (Int)
        prefix      - Optional  : prefix string             (Str)
        suffix      - Optional  : suffix string             (Str)
        barLen      - Optional  : character length of bar   (Int)
        fill        - Optional  : bar fill character        (Str)
    """
    curr_progress = 100 * (progress / float(progressLen))
    percent       = ("{0:.1f}").format(curr_progress)

    filledLength = int(barLen * progress // progressLen)
    bar          = fill * filledLength + '-' * (barLen - filledLength)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = "\r")

    # Print New Line on Complete
    if progress == progressLen: 
        print()