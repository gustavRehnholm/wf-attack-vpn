def print_progress_bar (progress, progress_len, prefix = '', suffix = '', bar_len = 50, fill = '█'):
    """
    Print progressbar
    Args:
        progress     - Required  : current progress          (int)
        progress_len - Required  : total iterations          (int)
        prefix       - Optional  : prefix string             (str)
        suffix       - Optional  : suffix string             (str)
        bar_len      - Optional  : character length of bar   (int)
        fill         - Optional  : bar fill character        (str)
    """
    curr_progress = 100 * (progress / float(progress_len))
    percent       = ("{0:.1f}").format(curr_progress)

    filledLength = int(bar_len * progress // progress_len)
    bar          = fill * filledLength + '-' * (bar_len - filledLength)

    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = "\r")

    # Print New Line on Complete
    if progress == progress_len: 
        print()