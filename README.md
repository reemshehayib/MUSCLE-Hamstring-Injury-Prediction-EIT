# MUSCLE-Hamstring-Injury-Prediction-EIT

**MUSCLE: Muscle Understanding through Synthetic Computation and Lesion Evaluation | A Semi-Synthetic Dataset for Hamstring Injury Prediction**

Using Electrical ImpedanceHamstring Injuries (HSI) are extremely common among athletes and require an extended rehabilitation period before the Return to Sport (RTS). After HSI, athletes go through a physical examination which in most cases is not enough to assess the severity of the injury or the rehabilitation process. Therefore, imaging techniques (such as Magnetic Resonance Imaging (MRI)) are usually employed which allow for a more detailed evaluation of the case at hand, and permits medical professionals to better assess the optimal rehabilitation process and time to RTS. Due to the impact HSI has on an athlete's career, it is essential to be able to predict it before its occurrence.    

Our work explores the use of Electrical Impedance Tomography (EIT) to predict hamstring injuries. To reach the goal of the study, a semi-synthetic dataset was created based on MRI scans of male patients with injured hamstring muscles. The boundaries of the hamstring group (the semimembranosus, the semitendanosus, and the biceps femoris) were determined and used to develop the dataset using Electrical Impedance Tomography and Diffuse Optical Tomography Reconstruction Software (EIDORS). By providing the boundaries of the hamstring muscles and setting the right properties, EIDORS generates EIT voltage measurements which result in the creation of the semi-synthetic dataset.    

To validate this dataset, Machine Learning (ML) models were  developed to test the ability of differentiating between injured and healthy hamstrings. The best performing model was a Random Forest (RF) model which reached an accuracy of 98% highlighting the capabilities of using EIT for the prediction of hamstring injuries.  

![image](https://github.com/user-attachments/assets/d403c383-11b6-4720-8dce-4a0383eea41a)
