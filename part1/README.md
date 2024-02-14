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
```
~/Documents/k8/part1/1.02 (master*) » docker run --rm waffle4everyone/serverpy         vanya@localhost
 * Serving Flask app 'server.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
```
### Exercise 1.03
» kubectl apply -f manifests/deployment.yaml       vanya@localhost
deployment.apps/log-output-dep created
~/.kube » kubectl logs log-output-dep-79b55d4669-4v5xc                                     vanya@localhost
17:10:41: bce55f32438852b4e7bc12a092b7cde8
17:10:46: bce55f32438852b4e7bc12a092b7cde8
17:10:51: bce55f32438852b4e7bc12a092b7cde8
17:10:56: bce55f32438852b4e7bc12a092b7cde8
17:11:01: bce55f32438852b4e7bc12a092b7cde8
~/.kube » kubectl rollout restart deployment log-output-dep                            1 ↵ vanya@localhost
deployment.apps/log-output-dep restarted
-----------------------------------------------------------------------------------------------------------
~/.kube » kubectl get pods                                                                 vanya@localhost
NAME                              READY   STATUS              RESTARTS   AGE
log-output-dep-79b55d4669-4v5xc   1/1     Running             0          5m
log-output-dep-56996c96df-57d8q   0/1     ContainerCreating   0          2s
-----------------------------------------------------------------------------------------------------------
~/.kube » kubectl get pods                                                                 vanya@localhost
NAME                              READY   STATUS        RESTARTS   AGE
log-output-dep-56996c96df-57d8q   1/1     Running       0          8s
log-output-dep-79b55d4669-4v5xc   1/1     Terminating   0          5m6s
-----------------------------------------------------------------------------------------------------------
~/.kube » kubectl get pods                                                                 vanya@localhost
NAME                              READY   STATUS    RESTARTS   AGE
log-output-dep-56996c96df-57d8q   1/1     Running   0          56s
### Exercise 1.04
```
~/Documents/k8/part1/1.04 (master*) » kubectl logs pod/todo-app-dep-8458fb8f9d-qfpgx   vanya@localhost
 * Serving Flask app 'server.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8000
Press CTRL+C to quit
```
### Exercise 1.05