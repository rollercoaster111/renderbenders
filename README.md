![PEARC21.](/cropped-PEARC21_Logo-1.png "Conference Logo - PEARC21.")
# Team Render Benders
The importance of rendering three-dimensional objects cannot be understated. Displaying an animated version of a dataset can open a door to the public to better comprehend the research being done, and data visualization has often been the difference between research teams which have received funding and which ones have not. Our team has chosen to direct our efforts towards rendering carbon nanotubes, which have been highlighted as a nanomaterial structure due to their high tensile strength and flexibility. Furthermore, in recent years, there have been multiple research advances highlighting the use of oriented carbon nanotubes for water filtration and oil adsorption from water. This is where Team Render Benders comes into action. Our team aims to provide accurate renders of the carbon nanotubes, first of one, and then of an orientation similar to those within the research advances mentioned above.
<!--- ![Render Benders Team Background.](/Team_Background.jpg "Hackathon Team Background - PEARC21.") -->
<p align="center">
  <img width="1100" height="600" src="https://github.com/rollercoaster111/renderbenders/blob/main/Team_Background.jpg">
</p>


# Dataset
The data file which our team is looking at is linked in the website here: https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes.

## Download and Installation

To begin using this template, choose one of the following options to get started:

- Clone the repo: `git clone https://github.com/rollercoaster111/renderbenders.git`
- [Fork, Clone, or Download on GitHub](https://github.com/rollercoaster111/renderbenders)

# Use CloudyCluster in the Project
CloudyCluster supports the dynamic provisioning and de-provisioning of HPC environment within commercial clouds. The provisioned HPC cluster can include shared filesystems, NAT instance, compute nodes, parallel filesystem, login node, and schedulers, and can solve storage issues for Big Data and Data Intensive applications. To improve the scalability of our RenderBender system, we deployed our system in CloudyCluster. Below is the overview of RenderBender. 

<p align="center">
  <img src="https://github.com/rollercoaster111/renderbenders/blob/main/RenderBenderOverview.jpg">
</p>

<p align="center">
  Fig. 1: The overview of RenderBender
</p>

Figure 1 shows the overview of RenderBender. The Utility layer shows the control node, login instance, scheduler instance and the GCSBucket (Google Cloud Storage bucket). The orangefs layer shows the OrangeFS instance. Torque and Slurm are job schedulers used to start, hold, monitor and cancel jobs submitted via the CloudyCluster interface. CloudyCluster Queue (CCQ) is a meta-scheduler provided with CloudyCluster that handles the instance selection and scaling the passes off the jobs to the configured scheduler (e.g., Torque or Slurm). A script is a set of instructions that specify how a job should be executed. RenderBender uses the script (e.g., Torque script, Slurm script) to specify how a job should be executed (including the number of requested nodes, the number of tasks on each node, etc.). 
<p align="center">
  <img src="https://github.com/rollercoaster111/renderbenders/blob/main/Script4RunJobs.jpg">
</p>

<p align="center">
  Fig. 2: An example of the script for specifying how a job should be executed
</p>

Figure 2 shows one of the configurations (an example of the script) for specifying how a job should be executed. RenderBender uses Torque/Maui HPC Scheduler and requests two nodes from the system (each node is assigned two tasks) by uncommenting “##PBS -l nodes=2:ppn=2”; RenderBender uses Slurm  HPC Scheduler and requests two nodes from the system (each node is assigned two tasks) by uncommenting “##SBATCH -N 2” and “##SBATCH --ntasks-per-node=2”. RenderBender uses the openMPI by uncommenting “#module add openmpi/3.0.0”.

In RenderBender, when users submit their jobs (e.g., animating the render), the jobs are delivered to the scheduler. The scheduler will split the jobs into tasks and distribute the tasks to the requested nodes from the system. Then the nodes run the tasks assigned to them and generate the result. The result will be saved in the location specified in the above script. Figure 3 shows the framework of job scheduling in RenderBender.
<p align="center">
  <img width="600" height="280" src="https://github.com/rollercoaster111/renderbenders/blob/main/JobScheduling.jpg">
</p>

<p align="center">
  Fig. 3: The framework of job scheduling in RenderBender
</p>

# Experimental Results

<p align="center">
  <img width="600" height="245" src="https://github.com/rollercoaster111/renderbenders/blob/main/cnt1-blue.png">
</p>

<p align="center">
  Fig. 4: Carbon nanotubes
</p>

<p align="center">
  <img width="600" height="280" src="https://github.com/rollercoaster111/renderbenders/blob/main/cnt1.png">
</p>

<p align="center">
  Fig. 5: Carbon nanotube
</p>

<p align="center">
  <img width="600" height="280" src="https://github.com/rollercoaster111/renderbenders/blob/main/render1.png">
</p>

<p align="center">
  Fig. 6: Render the Blender files
</p>

<p align="center">
  <img width="600" height="280" src="https://github.com/rollercoaster111/renderbenders/blob/main/render2.png">
</p>

<p align="center">
  Fig. 7: Render the Blender files
</p>

<p align="center">
  <img width="600" height="280" src="https://github.com/rollercoaster111/renderbenders/blob/main/render3.png">
</p>

<p align="center">
  Fig. 8: Render the Blender files
</p>

<p align="center">
  <img width="600" height="280" src="https://github.com/rollercoaster111/renderbenders/blob/main/templates/images/0010.png">
</p>

<p align="center">
  Fig. 9: Render the Blender files
</p>

We also recorded the demonstration of some experiments, and we posted it to YouTube. Here is the link of one of our demonstrations: https://youtu.be/2nILAXKG-QU.

# Research Findings
The articles depicting the different research findings are linked here: https://interestingengineering.com/nanofiber-membrane-filters-999-of-salt-from-seawater-within-minutes, https://interestingengineering.com/new-porous-yet-sturdy-mat-can-adsorb-25-times-its-weight


The software programs our team is using to visualize the carbon nanotubes and their orientations are Blender and CASTEP, and we fully intend to use CloudyCluster to render our models faster and demonstrate the efficiency of our models. 


