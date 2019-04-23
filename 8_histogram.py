class histogramDemo:
    def histogram( values ):
         for val in values:
            histValues = ''
            times = val
            while( times > 0 ):
                histValues = histValues + '*'
                # histValues += '*'
                times = times - 1
            print(histValues)

    histogram([2, 1, 9, 5])