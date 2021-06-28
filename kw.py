#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
cmd1 = f.getvalue("y")
cmd2 = f.getvalue("a")
cmd3 = f.getvalue("b")
cmd4 = f.getvalue("c")

if ( ("deployment" in cmd) or ("deploy" in cmd) or ("deployments" in cmd) ) and ("image" in cmd):
  cmd = "kubectl create deployment"+ " " + cmd1 + " " + "--image=" + cmd4 + " --kubeconfig admin.conf"
  o = sp.getoutput("sudo " + cmd)
  print(o)

elif ("pods" in cmd) and ("show" in cmd):
  o = sp.getoutput("sudo kubectl get pods --kubeconfig admin.conf")
  print(o)

elif ( ("deployment" in cmd) or ("deploy" in cmd) or ("deployments" in cmd) ) and ("show" in cmd):
  o = sp.getoutput("sudo kubectl get deployments --kubeconfig admin.conf")
  print(o)

elif ("expose" in cmd) and ( ("deployment" in cmd) or ("deploy" in cmd) or ("deployments" in cmd) ):
  cmd = "kubectl expose deployment" + " " + cmd1 + " " + "--port=" + cmd2 + " --type=NodePort --kubeconfig admin.conf"
  o = sp.getoutput("sudo " + cmd)
  print(o)

elif ("scale" in cmd) and ( ("replicas" in cmd) or ("replica" in cmd) ):
  cmd = "kubectl scale deployment" + " " + cmd1 + " " + "--replicas=" + cmd3 + " --kubeconfig admin.conf"
  o = sp.getoutput("sudo " + cmd)
  print(o)

elif ("delete" in cmd) and ( ("deployment" in cmd) or ("deploy" in cmd) or ("deployments" in cmd) ):
  cmd = "kubectl delete deployment" + " " + cmd1 + " " + "--kubeconfig admin.conf"
  o = sp.getoutput("sudo " + cmd)
  print(o)
