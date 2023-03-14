
I know that there is only Resource Manager in a hadoop cluster. From my understanding, there should be only one Application Master for a cluster as well. Is that right? Following is my understanding of how a mapreduce job is run in YARN. Please correct if my understanding is not right.

Application execution sequence of steps on YARN:

- Client submits a job to the Resource Manager (RM). RM runs on Master Node. There is only one RM across the cluster to manage the        resources. Resource Manager is a Daemon process.
- RM will go to HDFS thru Name Node.
- RM spins up an Application Master (AM). AM will reach HDFS thru Name Node. It will create a mapper matrix. This is the mapper phase. Like if Block 1 is available on Name Node 5 or 6.
- Based on Mapper matrix information, AM sends requests to individual Node managers (NM) to run a particular task for each block. NM runs on slave node.
- Each NM sends a request to RM to get a container. A container executes an application specific process with a constrained set of resources (memory, CPU etc).
- Mapper task runs in the container and sends the heart beat to the Application master. AM also sends the heart beat to RM.
After all the processes are done, AM starts another matrix for Reducer tasks.
- After all the reducer tasks are completed, the AM sends the results to RM.
- RM lets the client know the results and kills the AM. Application Master can get stuck. That is why it is sending heart beats to Resource Manager

-  The AM can only execute inside any given container. So first the RM requests a node manager on some node to start a container and then only the AM gets launched inside that cotainer, not before. So there will be a container dedicated to the AM.