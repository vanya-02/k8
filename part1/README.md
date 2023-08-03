# Part 1
### Exercise 1.01

Commands used:
```
docker build --push -t waffle4everyone/logoutput .
k3d image import waffle4everyone/logoutput
# To renew the old image with a new one:
kubectl scale --replicas=0 deployment log-output
kubectl scale --replicas=1 deployment log-output
kubectl logs -f log-output-66d9cd78dd-x95jh
```
Output:
```
15:41:12: f64a249fc738d7aaf1f386add89d1df6
15:41:47: f64a249fc738d7aaf1f386add89d1df6
15:41:52: f64a249fc738d7aaf1f386add89d1df6
15:41:57: f64a249fc738d7aaf1f386add89d1df6
15:42:02: f64a249fc738d7aaf1f386add89d1df6
15:42:07: f64a249fc738d7aaf1f386add89d1df6
15:42:12: f64a249fc738d7aaf1f386add89d1df6
```
### Exercise 1.02