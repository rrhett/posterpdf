import argparse
import os
import subprocess
import utils

parser = argparse.ArgumentParser(description="Posterify a pdf")
parser.add_argument("-i", "--input", required=True, help="Input PDF")
parser.add_argument("-o", "--output", required=True, help="Output PDF")
parser.add_argument("-n", required=True, type=int, help="Number of pages in PDF")
parser.add_argument("-s", required=True, type=int, help="Start on this page")
parser.add_argument("-e", action="store_true", help="End page is single")
args = parser.parse_args()

# Store these files as temporary files
t_files = []
pb = utils.ProgressBar(args.n - args.s + 1)
for p in range(args.s, args.n + 1):
  pb.tick()
  tf = f"tmp_{p}.pdf"
  of = f"tmpo_{p}.pdf"
  t_files.append(of)
  subprocess.run(["pdftk", args.input, "cat", str(p), "output", tf], check=True)
  if p == args.n and args.e:
    subprocess.run(["cp", tf, of])
  else:
    subprocess.run(["mutool", "poster", "-x", "2", tf, of], check=True)
  os.remove(tf)

cmd = ["pdftk"]
cmd.extend(t_files)
cmd.append("cat")
cmd.append("output")
cmd.append(args.output)

subprocess.run(cmd, check=True)

for tf in t_files:
  os.remove(tf)

