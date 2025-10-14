import ROOT
ROOT.gROOT.SetStyle('Plain')


INPUT_FILE_PATH = 'data/pendolo.txt'
OUTPUT_FILE_PATH = 'data/pendolo.tex'
NUM_TABLE_COLS = 7


h = ROOT.TH1F('h', 'h', 14, 19.8, 20.8)
vals = []

print('Reading input file %s...' % INPUT_FILE_PATH)
for line in open(INPUT_FILE_PATH):
    line = line.strip('\n')
    if not line.startswith('#') and len(line):
        val = float(line)
        vals.append(val)
        h.Fill(val)
print('Done. %d value(s) found.' % len(vals))

vals.sort()
h.Draw()
f = ROOT.TF1('f', 'gaus')
h.Fit('f')
ROOT.gPad.Update()

print('Fit chisquare = %.3f/%d' % (f.GetChisquare(), f.GetNDF()))

outputFile = open(OUTPUT_FILE_PATH, 'w')

def write(stuff):
    outputFile.write(stuff)

fmt = 'l' * NUM_TABLE_COLS
write('\\begin{tabular}{%s}\n' % fmt)
write('\\hline\n')
numRows = int(len(vals)/NUM_TABLE_COLS - 0.0001) + 1
for row in range(numRows):
    text = ''
    for col in range(NUM_TABLE_COLS):
        i = row + numRows*col
        try:
            val = vals[i]
            text += '\makebox[28pt]{\hfill[%d]}~%.3f & ' % (i + 1, val)
        except:
            pass
    text = text.strip(' &')
    write('%s\\\\\n' % text)
write('\\hline\n') 
write('\\end{tabular}\n')
outputFile.close()



