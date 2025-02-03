# Paper 1

**Title**: "Tor Traffic Analysis and Detection via Machine Learning Techniques"  
**Method**: Machine learning classifiers analyze 23 network-based features to differentiate Tor traffic and its activities from non-Tor traffic.  
**Dataset**: Real-world network traffic (22GB) captured via Wireshark and tcpdump, categorized into Tor and non-Tor traffic across 8 application types.  
**Result**: jRip classifier achieves perfect classification with precision and recall values of 1.0 for Tor traffic detection.  
**Limitations**: Limited exploration of scalability to cloud environments and other anonymizing technologies.

**Dataset Description**:  
The dataset comprises 22GB of labeled network traffic collected from real-world applications. Traffic is categorized into Tor and non-Tor data across 8 types: browsing, email, chat, audio streaming, video streaming, FTP, VoIP, and P2P. Tools like Wireshark and tcpdump capture both normal and Tor-routed traffic at a gateway and workstation. Bidirectional flows are processed with ISCXFlowMeter, extracting time-related and statistical features, including flow inter-arrival times and packet rates. The labeled dataset includes more than 18 applications like Gmail, Skype, and Spotify, ensuring comprehensive traffic representation.

**Method Description**:  
The approach utilizes machine learning to classify Tor and non-Tor traffic based on 23 extracted flow features. The pipeline begins with preprocessing and feature extraction using ISCXFlowMeter. Classifiers such as jRip, J48, and BayesNet are evaluated with a 10-fold cross-validation strategy. Each classifier processes labeled traffic to identify Tor usage and categorize activity types (e.g., VoIP, streaming). The model is tested on unseen data to ensure robustness, employing metrics like precision, recall, F-measure, and ROC area for performance assessment. Tools like Weka facilitate implementation.

**Result Description**:  
The jRip algorithm delivered exemplary results, achieving 100% precision and recall for Tor traffic classification. Other algorithms like J48 also performed well, with precision and recall values near 0.998. The method effectively distinguished activity types within the Tor network, such as email and P2P traffic. False-positive rates were minimal across classifiers, and computational efficiency was maintained, with average processing times below five seconds. The feature set proved statistically significant in discriminating Tor and non-Tor traffic.

#### 

**Total Paper Summary**

This study presents a machine learning-based framework to analyze and detect Tor network traffic, addressing the growing misuse of Tor for illicit activities. The proposed approach employs a feature set of 23 flow-level metrics, such as inter-arrival times and flow durations, to classify traffic as Tor or non-Tor. The dataset, comprising 22GB of real-world traffic labeled into 8 activity categories, was processed with ISCXFlowMeter to extract relevant features. Machine learning classifiers, including jRip and J48, were trained and evaluated using a 10-fold cross-validation approach.

The framework demonstrated exceptional performance, with the jRip classifier achieving 100% precision and recall in identifying Tor traffic. It also successfully categorized activities like browsing and streaming within the Tor network. The analysis achieved high accuracy with minimal false positives, maintaining computational efficiency. However, the study’s scope is limited to specific scenarios, lacking evaluation in broader application environments like cloud platforms or alternative anonymizing networks.

Future research aims to incorporate formal methods, extend applicability to cloud environments, and optimize the system for efficiency using synopsis-oriented paradigms. This paper provides a robust, adaptable machine learning framework that advances the field of network security and traffic analysis.

# Paper 2

**Title:** Machine Learning Based Classification of IoT Traffic  
**Method:** Comparison of 4 ML algorithms and 3 Neural Networks (NNs) for IoT traffic classification under different undersampling strategies.  
**Dataset:** IoTID20 dataset with 625,783 instances of IoT network traffic categorized as normal or anomalous.  
**Result:** XGBoost outperformed other methods, achieving near-perfect accuracy; NNs struggled under reduced data scenarios due to parameter optimization challenges.  
**Limitations:** The dataset was simulated, limiting real-world applicability; future research requires testing on real-time data and extending to multiclass classification.

**Dataset Description:**

The IoTID20 dataset comprises 625,783 instances of network traffic captured in a smart home environment. It features data from devices such as speakers, smartphones, security cameras, and laptops. The dataset categorizes traffic into normal (40,073 instances, 6.4%) and anomalous (585,710 instances, 93.6%), further subdivided into attack types: DoS, Mirai, MITM, and Scan. Eighty-three network features, such as flow duration, protocol type, and packet counts, were extracted, along with three labels representing binary, category, and sub-category traffic classifications. Preprocessing removed missing values, irrelevant features like IP addresses and timestamps, and balanced the dataset using RandomUnderSampler, retaining 40,073 samples for each class.

**Method Description:**  
This study evaluated the performance of 4 classic ML algorithms (Gaussian Naive Bayes, Support Vector Classifier, Random Forest, XGBoost) and 3 NNs with varying depths (1, 2, and 4 hidden layers) for IoT traffic classification. Preprocessing involved cleaning and normalizing the data, followed by splitting it into 80% training and 20% testing subsets. Six sampling strategies were applied to simulate data reduction, ranging from the original dataset to fully balanced subsets. Models were trained and evaluated using metrics like accuracy, precision, recall, and F1-score. XGBoost demonstrated resilience to data reduction, while NNs underperformed with undersampled data due to challenges in parameter tuning.

**Result Description:**  
XGBoost achieved the highest accuracy (\~100%) for IoT traffic classification, maintaining performance across all sampling strategies. Random Forest and Support Vector Classifier also performed well but showed declines under undersampling. NNs exhibited near-perfect accuracy with the original dataset but failed to adapt to reduced data due to the need for extensive parameter optimization. For instance, the 4-layer NN’s accuracy dropped from 93.53% with the full dataset to 39.39% with maximally reduced data. These results highlight the robustness of ensemble methods like XGBoost over NNs in data-limited scenarios.

**Total Paper Summary:**  
This research investigates machine learning (ML) and deep learning (DL) methods for IoT traffic classification, emphasizing their performance under data reduction. Using the IoTID20 dataset, 4 classic ML algorithms (Gaussian Naive Bayes, Support Vector Classifier, Random Forest, XGBoost) and 3 Neural Networks (NNs) were evaluated for binary traffic classification. Preprocessing balanced the data using RandomUnderSampler, simulating scenarios with reduced anomalous traffic. XGBoost consistently outperformed other models, achieving near-perfect accuracy across all sampling strategies. Random Forest and Support Vector Classifier displayed moderate declines under undersampling, while NNs struggled significantly, with accuracy for the 4-layer NN dropping from 93.53% to 39.39%. The study concluded that ML algorithms like XGBoost are better suited for handling data scarcity in IoT applications. Limitations include the use of simulated data, emphasizing the need for future studies on real-world datasets and multiclass classification tasks. This work provides a foundational understanding of IoT traffic modeling and highlights XGBoost’s robustness in imbalanced data environments.

# Paper 3

**Title:** IoT Network Traffic Analysis with Deep Learning  
**Method:** Ensemble model combining CNN+LSTM and Random Forest with pre-trained KNN for IoT anomaly detection.  
**Dataset:** KDD Cup 1999 dataset (10%), consisting of 494,021 instances with normal and attack traffic categories.  
**Result:** The ensemble model achieved 98.22% accuracy, outperforming individual AutoEncoder and GAN models.  
**Limitations:** Dataset was simulated and outdated; future work requires testing on contemporary real-world IoT datasets.

**Dataset Description:**  
The study used the 10% version of the KDD Cup 1999 dataset, which includes 494,021 entries with 42 attributes representing network traffic. This benchmark dataset contains simulated data from a military network and includes both normal and various attack types: DoS, Probe, R2L, and U2R. The training set comprised 77,815 normal and 313,163 DoS attack samples, while the test set had a similar distribution. Preprocessing steps included handling missing values, encoding categorical variables using one-hot and label encoding, and applying normalization through MinMaxScaler. The dataset's representative nature and sufficient size make it ideal for training deep learning models, but its age and simulated nature pose challenges for current IoT applications.

**Method Description:**  
The proposed ensemble method integrates CNN, LSTM, and Random Forest classifiers for IoT anomaly detection. The pipeline starts with a KNN layer for initial categorization, followed by a CNN+LSTM model to analyze sequential data patterns and a Random Forest classifier to resolve conflicting classifications. The CNN+LSTM model utilized 20 epochs and a batch size of 128, while the Random Forest layer was fine-tuned using validation data. The GAN and AutoEncoder models were also implemented for comparison. Preprocessing involved scaling, normalization, and hyperparameter optimization. Metrics such as accuracy, precision, recall, and F1-score were used for evaluation. The ensemble model demonstrated robustness in handling both normal and anomalous data by combining the strengths of individual models.

**Result Description:**  
The ensemble model outperformed standalone AutoEncoder and GAN models in anomaly detection tasks. It achieved an accuracy of 98.22%, with precision, recall, and F1-scores of 92.67%, 96.68%, and 96.21%, respectively. The CNN+LSTM model contributed significantly to sequence pattern recognition, while the Random Forest layer resolved inconsistencies from preceding models. Compared to AutoEncoder (accuracy: 97.96%) and GAN (accuracy: 90.28%), the ensemble model minimized false positives and negatives, as evidenced by its confusion matrix. These results highlight the potential of ensemble techniques in achieving high accuracy and robust performance for IoT anomaly detection.

**Total Paper Summary:**  
This research presents a deep learning-based ensemble model for IoT network anomaly detection, addressing the challenges of real-time data monitoring in complex IoT environments. Leveraging the KDD Cup 1999 dataset, the study integrates CNN+LSTM and Random Forest classifiers with a pre-trained KNN layer for robust anomaly detection. The dataset underwent comprehensive preprocessing, including encoding and normalization. The ensemble model achieved an accuracy of 98.22%, outperforming standalone models like AutoEncoder (97.96%) and GAN (90.28%). It demonstrated high precision, recall, and F1-scores, effectively minimizing false positives and negatives. Despite the outdated and simulated nature of the dataset, the study highlights the effectiveness of ensemble methods in anomaly detection. Future work should focus on validating the model on real-world IoT datasets and exploring its scalability. This research establishes a strong foundation for developing advanced IoT security frameworks, emphasizing the potential of deep learning and ensemble techniques.

# Paper 4

**Title:** Design of an Efficient Forensic Layer for IoT Network Traffic Analysis Engine Using Deep Packet Inspection via Recurrent Neural Networks  
**Method:** Deep packet inspection combined with LSTM and GRU-based RNNs for IoT attack detection and analysis.  
**Dataset:** IoT-23, CICIDS2017, IoT-Traffic, and UNSW-NB15 datasets combined into a unified dataset of 900,000 records.  
**Result:** The proposed model achieved 98.3% accuracy, 97.5% precision, and 98.9% recall, outperforming ADGCN, LDNN, and FDRL models.  
**Limitations:** Limited scalability; future work requires testing in real-world deployments and handling resource constraints of IoT devices.

**Dataset Description:**  
Four datasets were used:

1. **IoT-23 Dataset:** Simulated IoT environment traffic, including normal and malicious interactions from various IoT devices.  
2. **CICIDS2017 Dataset:** A comprehensive set of labeled network traffic data focusing on IoT attacks and other malicious behaviors.  
3. **IoT-Traffic Dataset:** Network captures from different IoT devices, encompassing benign and malicious traffic patterns.  
4. **UNSW-NB15 Dataset:** General network traffic dataset with diverse attack scenarios, not specific to IoT.

These datasets were fused to create a comprehensive dataset of 900,000 records. The fused data included 200,000 records for validation, 600,000 for training, and 100,000 for testing. Preprocessing involved feature extraction from network packets, including protocol, source and destination addresses, timestamps, and other parameters critical for traffic analysis.

**Method Description:**  
The proposed model integrates deep packet inspection with RNNs, leveraging LSTM and GRU architectures for IoT network traffic analysis. DPI extracts metadata from packets, including protocol, source and destination addresses, port numbers, timestamps, and payload characteristics. Temporal dependencies in the data are captured using LSTM and GRU, making the model effective for time-series analysis.  
The workflow includes:

1. **Feature Extraction:** Parameters such as packet length, flags, and QoS markings are extracted.  
2. **Feature Encoding:** Temporal data is encoded into feature sets processed by RNN layers.  
3. **Classification:** An RNN-based SoftMax layer classifies traffic into normal or attack types.

The model uses hyperparameter tuning, including adjustments for learning rate, epochs, and batch size. Performance was evaluated against metrics such as precision, accuracy, recall, and delay. Comparison with ADGCN, LDNN, and FDRL demonstrated the model's superior performance in real-time attack detection.

**Result Description:**  
The proposed model achieved:

* **Precision:** 97.5%  
* **Accuracy:** 98.3%  
* **Recall:** 98.9%  
* **Reduced Delay:** Outperformed ADGCN, LDNN, and FDRL in processing speed by 12.2%.

Compared to existing methods, the model demonstrated superior attack detection rates, reduced false positives and negatives, and maintained high accuracy under diverse attack scenarios. Key advancements include its ability to classify multiple attack types, robust temporal feature extraction, and adaptability to high-variance network traffic.

**Total Paper Summary:**  
This study introduces an advanced IoT network traffic analysis framework using deep packet inspection (DPI) combined with LSTM and GRU-based recurrent neural networks (RNNs). Leveraging DPI, the model extracts features like protocol type, timestamps, and payload size to characterize IoT traffic. LSTM and GRU components capture temporal dependencies, enabling effective detection of attacks in sequential data. The model was evaluated on a fused dataset of 900,000 records from IoT-23, CICIDS2017, IoT-Traffic, and UNSW-NB15 datasets.  
Achieving 98.3% accuracy, 97.5% precision, and 98.9% recall, the model outperformed state-of-the-art methods such as ADGCN, LDNN, and FDRL. Key features include its high variance feature extraction, superior temporal modeling, and reduced latency in attack detection. Despite its strengths, the model requires validation in real-world IoT deployments and optimization for resource-constrained devices. Future work will explore scalability, domain adaptation, and integration of real-time threat intelligence. This research offers a significant contribution to IoT security, providing a robust tool for real-time network analysis and attack prevention.

# 

# Paper 5

**Title**: IoT Devices Recognition Through Network Traffic Analysis  
**Method**: Machine learning classifiers analyze bidirectional flow features to classify IoT devices, using Random Forest and five other algorithms.  
**Dataset**: Network traffic data collected over 7 days from a smart home network with four IoT devices.  
**Result**: Random Forest achieved 99.9% accuracy in recognizing IoT devices based on their network traffic.  
**Limitations**: Limited dataset with only four IoT devices; challenges in scalability to larger and mixed-purpose networks.

# 

**Dataset Description:**  
The dataset was collected from a smart home network consisting of four IoT devices: a Nest security camera, a D-Link motion sensor, a TP-Link smart bulb, and a TP-Link smart plug. Data were collected over 7 days, yielding 3222 bidirectional flows for training and 805 flows for testing. A Raspberry Pi, placed between the access point and the internet, captured the network traffic. Each bidirectional flow was labeled using MAC addresses and preprocessed to extract only TCP flows, as the devices communicated via HTTP or HTTPS. Features extracted include the size of the first 10 packets sent and received and their inter-arrival times. The dataset lacks diversity and size, which limits its applicability to larger IoT ecosystems.

**Method Description:**  
The study employed six machine learning classifiers (Random Forest, Decision Tree, SVM, k-Nearest Neighbors, ANN, and Gaussian Naive Bayes) to classify IoT devices based on their network behavior. Features extracted from bidirectional flows were used to train the models. Random Forest emerged as the best performer, achieving near-perfect accuracy. Visualization using t-SNE showed distinct clusters for each device, validating the effectiveness of the selected features. Metrics like accuracy, precision, recall, and F1-score were used for evaluation, with Random Forest achieving 99.9% accuracy and ANN performing slightly lower at 98.6%.

**Result Description:**  
Random Forest achieved 99.9% accuracy, with perfect precision and recall for most devices. The ANN classifier reached 98.6%, while Gaussian Naive Bayes performed the worst with 91.9% accuracy. Feature importance analysis revealed that even a reduced feature set could maintain high accuracy due to the predictable nature of IoT device traffic. The study demonstrated the feasibility of identifying IoT devices with high accuracy, although performance might degrade with more diverse device types or real-world noise.

Total Paper Summary:

This study presents a machine learning framework for recognizing IoT devices based on their network traffic, addressing the need for automated monitoring in smart environments. Using a smart home setup, the authors collected traffic data from four IoT devices over 7 days. Bidirectional flow features, including packet sizes and inter-arrival times, were extracted for classification. Six machine learning algorithms, including Random Forest and ANN, were evaluated, with Random Forest achieving 99.9% accuracy. Visualization using t-SNE revealed clear clusters for each device, confirming the discriminative power of the selected features. Despite its success, the study is limited by the small dataset and restricted device variety, challenging its scalability to real-world IoT networks. Future work should focus on expanding the dataset and validating the approach in mixed-purpose networks with diverse IoT devices.

# 

# 

# 

# 

# 

# 

# 

# 

# 

# Paper-6

# 

**Title**: Detecting Malicious Websites by Learning IP Address Features  
**Method**: Supervised machine learning approach using features extracted from IP addresses, evaluated with SVM classifiers.  
**Dataset**: IP addresses derived from blacklists, Alexa’s top 10,000 websites, and campus network traffic data.  
**Result**: The proposed method achieved 90.2% accuracy and 99.4% AUC, effectively identifying unknown malicious IPs.  
**Limitations**: Potential false positives for benign hosting services and limited scalability to larger datasets.

**Dataset Description:**  
The dataset consisted of three sources:

1. **Benign Data**: Alexa’s top 10,000 websites provided 10,372 IP addresses as benign samples, ensuring diversity by including file-sharing and less reputable sites. Campus network traffic over two weeks (57,190 IPs) also served as a benign dataset, verified using Google Safe Browsing to remove 2,515 malicious URLs.  
2. **Malicious Data**: IP addresses of 14,171 malicious websites from the Malware Domain List (MDL) spanning over two years (2009–2011). This data was divided into subsets: active malicious IPs and newly identified malicious IPs unseen during training.  
3. **Validation Data**: Campus traffic datasets and MDL entries formed the test sets for evaluating both known and unknown malicious IPs.

**Method Description:**

The study proposed a machine learning-based detection mechanism using IP address features such as octet-based, extended octet-based, and bit string-based extractions. Features were extracted from each IP address and fed into an SVM classifier with a Gaussian kernel. Training involved cross-validation and grid search to optimize hyperparameters. Metrics such as accuracy, false positive rate (FPR), false negative rate (FNR), and AUC (Area Under the Curve) were used for evaluation. Additionally, thresholds were adjusted for enhanced detection of unknown IPs, reducing false positives and negatives.

**Result Description:**

The extended octet-based feature extraction method (ExOctet) yielded the best performance with 90.2% accuracy, 99.4% AUC, and a low FPR of 0.098 for active malicious IPs. The model successfully identified unknown malicious IPs from the test set with minimal false positives. Compared to traditional intrusion detection systems like Snort, this approach demonstrated higher precision and reduced false alerts. Visualization techniques, such as Hilbert curves, further supported the spatial clustering of malicious IPs. The method showed robustness in generalizing to unseen IPs but struggled with false positives from benign hosting services due to shared IP usage.

**Total Paper Summary:**

This study introduces a novel machine learning framework to detect malicious websites using features derived from IP addresses. Unlike conventional approaches relying on URLs or DNS, this method capitalizes on the stability and address space patterns of IPs. The authors employed supervised learning, specifically SVM classifiers, with features extracted through octet-based, extended octet-based, and bit string-based methods. Using data from Alexa’s top websites, Malware Domain List, and campus network traffic, the framework was trained and tested to identify both known and unknown malicious IPs. The ExOctet feature extraction method achieved the best results, with 90.2% accuracy and 99.4% AUC, outperforming traditional systems like Snort in both precision and scalability.  
However, the study faces limitations, including high false positives for benign hosting services and challenges in extending the method to larger datasets or dynamic IP scenarios. Future research should focus on mitigating false positives and improving scalability. This work significantly enhances the detection landscape, offering a lightweight and scalable solution for malicious website detection while complementing existing blacklist systems.

# Paper 7

**Title**: Network Anomaly Detection Through IP Traffic Analysis With Variable Granularity.  
**Method**: Anomaly detection with Fast xFlow Proxy for deconstructing IP traffic and analysing anomalies using correlation value analysis and dynamic thresholds.  
**Dataset**: Synthetic traffic datasets created to mimic real-world large-scale network behaviours and anomalies.  
**Result**:The suggested method delivers near-perfect accuracy for large-scale anomalies and 80-90% accuracy for smaller fluctuations, even in noisy situations.  
**Limitations**: The method is based on synthetic data and struggles to find anomalous locations; real-world validation and fault localisation remain unsolved.

**Dataset Description**:   
The collection is made up of synthetic time-series traffic data created to imitate real-world network behaviours. Traffic is modelled as periodic patterns with external abnormalities superimposed, such as service outages (zero traffic) or security assaults (up to 100% traffic spike). The synthetic generator allows you to customise the region, service attributes, and anomaly scenarios (such as the length and scale of abnormalities). The dataset is used to assess performance with varied noise levels and sampling rates.

**Method Description**:

1. The article presents an anomaly detection method based on the Fast xFlow Proxy, which enables fine-grained traffic breakdown in large-scale IP networks. Key Steps:  
2. Traffic Decomposition: The Fast xFlow Proxy eliminates encapsulated outer IP headers, allowing for accurate inspection of individual flows.  
3. A simple correlation value study compares current time-series traffic patterns to previous patterns in order to find differences.  
4. Dynamic Thresholding: Thresholds adjust dynamically dependent on monitoring granularity and noise levels, providing for reliable anomaly identification in a variety of settings.  
5. Quasi-Real-Time Detection: To enable real-time anomaly detection, sliding-window methods are used, which continuously update as fresh traffic observations are made.  
   

**Result Description**:

1. Service failures are detected with nearly 100% accuracy when the sampling rate (SR) is high. Even with lower SRs, detection is possible.  
2. Traffic Increase Events: High-traffic anomalies (such as DDoS attacks) are effectively identified, but minor increases are more difficult to detect at low SRs.

**Total Paper Summary:**

The research, "Network Anomaly Detection Through IP Traffic Analysis With Variable Granularity," suggests a novel approach to identifying anomalies in large-scale, wide-area IP networks. This solution makes use of the Fast xFlow Proxy technology, which allows for fine-granular deconstruction of macroscopic traffic flows, hence improving anomaly detection accuracy. To identify abnormalities like service outages or DDoS attacks, the technique uses time-series traffic flow analysis, correlation computation, and dynamic thresholding.

The Fast xFlow Proxy can analyse encapsulated IP packets at extremely high speeds (up to 100 Gbps), allowing for thorough traffic monitoring. By analysing deconstructed traffic flows, the system finds anomalies based on regular traffic patterns. The study makes two significant contributions: demonstrating the efficacy of granular flow decomposition for anomaly detection and demonstrating the method's adaptability to a wide range of anomaly scenarios with an accuracy of 80-100%, even under difficult conditions such as high noise or minor traffic fluctuations.

The research assesses the method's performance using simulations and introduces a dynamic thresholding approach to improve detection accuracy. While beneficial, the study acknowledges limitations, such as the reliance on simulated traffic and the inability to localise anomalies, proposing further work in real-world traffic analysis and failure localisation.

# Paper 8

**Title**: A Real-Time DDoS Attack Detection and Prevention System Based on Per-IP Traffic Behavioral Analysis.  
**Method**: Per-IP traffic behavioural analysis is supplemented with a non-parametric CUSUM method.  
**Dataset**: Network traffic data collected from Chongqing University of Posts and Telecommunications' campus network.  
As a result, the system reliably detects and mitigates DDoS attacks in real time at their early phases.  
**Limitations**: The system's effectiveness is dependent on its deployment environment, and it requires additional testing for scalability under various assault scenarios.

**Dataset Description**:   
This dataset includes real-time traffic data from Chongqing University's campus network. It contains TCP, UDP, and ICMP protocol communication. The data characteristics include SYN, ACK, and RST packet counts for each IP address, allowing the system to track protocol synchronisation behaviour. It includes traffic from both normal operations and assault simulations, with different rates of SYN flooding attacks.

**Method Description**:  
Traffic Behavioural Analysis: Each IP's transmitting and receiving behaviour is analysed for synchronisation irregularities.  
CUSUM method: A non-parametric variant of the CUSUM method uses packet behaviour during given time periods to identify IP addresses as attackers, victims, or normal users.  
Packet classification and filtering: A hash-based categorisation divides traffic into three categories: observed, safe, and alarmed. Once recognised, attack traffic is screened, and valid packets are transmitted.

**Result Description**:  
The technology accurately recognised SYN flooding assaults across numerous traffic circumstances. Detection happened during the early stages of an attack, with response times ranging from 1-2.5 minutes for attack identification and mitigation. The system maintained a low computing overhead and proved the capacity to distinguish between legal traffic bursts and malicious traffic.

**Total Paper Summary:**

The paper describes a real-time system for identifying and combating Distributed Denial of Service (DDoS) assaults, with a focus on per-IP traffic behaviour analysis. This system is installed at a leaf router near the victims and watches each IP user's traffic to detect odd behaviour. It uses statelessness and little computing overhead to ensure robustness against flooding attacks. The system uses TCP and UDP protocol synchronisation, as well as a non-parametric CUSUM technique, to identify SYN flooding assaults efficiently. It categorises IP users as attackers, victims, or normal users and performs real-time operations like blocking attackers and permitting genuine traffic.

The architecture consists of three layers: application, network, and driver. It supports user-friendly operations, quick data processing, and real-time traffic filtering. A packet categorisation approach decreases memory usage and computation, whilst flood feature extraction improves in spotting synchronisation issues between traffic behaviours. Experimental results on a college network proved the system's capacity to detect and prevent early-stage threats with high accuracy and low latency. Beyond SYN flooding, it can detect DNS flooding and Smurf assaults, demonstrating its broad usefulness. The suggested system's design guarantees scalability and efficient real-time reaction, addressing fundamental issues in online DDoS attack detection and prevention.

# Paper 9

**Title**: I2P Anonymous Traffic Detection and Identification.  
**Method:** I2P traffic is detected and classified using four supervised classification algorithms (NaiveBayes, BayesNet, SVM, and RandomForest) based on traffic attributes.  
**Dataset**: I2P network traffic data obtained using virtual machines, Wireshark, and RouterInfo.RandomForest attained the best classification accuracy (100%) through excellent feature selection.  
**Limitations**: include a limited consideration of encryption principles and the impact of feature selection; the focus is solely on four algorithms, with no exploration of advanced approaches.

**Dataset Description**:   
The collection includes network traffic data from I2P anonymous services such as file sharing, chat, and servers. It was gathered in a controlled environment using Wireshark to capture tunnel data and RouterInfo files for labelling. To optimise classification performance, various traffic features, such as IP, packet length, and inter-arrival durations, were extracted, with feature subsets reduced from 74 to 22 attributes.

**Method Description**:  
The study used four supervised classification algorithms:

1. NaiveBayes is simple but constrained because to its independence assumptions.  
2. BayesNet is a probabilistic model that uses directed acyclic graphs to represent feature interdependencies.  
3. SVM is a kernel-based model for vector classification.  
4. RandomForest is a decision tree-based ensemble method for making robust predictions. Tranalyzer2 was used for feature selection, with tests comparing subsets of 74, 51, and 22 features to see how they affected classification accuracy.

**Result Description**:  
The trials revealed that RandomForest is the most successful algorithm, reaching 100% accuracy with the smallest feature subset (22 features). BayesNet also performed well, especially when cross-validated. Naive Bayes and SVM performed poorly because of feature independence assumptions and poor adaptability to decreased feature sets. The study focusses on the trade-offs between feature selection and algorithm performance.

**Total Paper Summary:**

The research focuses on identifying and classifying activity in the Invisible Internet Project (I2P), a peer-to-peer anonymous communication network. I2P facilitates secure connection by concealing users' identities, and it is commonly used for private browsing, file sharing, and other purposes. The study's goal is to identify I2P traffic in order to improve network security and track its usage.

The authors investigate the I2P communication protocol, namely NTCP (I2P's secure TCP-based protocol), and employ payload length patterns for early traffic filtering. They use supervised machine learning methods such as NaiveBayes, BayesNet, SVM, and Random Forest to classify traffic. Data gathering consists of monitoring I2P tunnels and labelling traffic datasets by analysing node communication and correlating it with router information.

Experimental findings show that Random Forest outperforms other algorithms, obtaining 100% accuracy and F-measure in some situations. Experiments with feature reduction reveal that lowering traffic features increases classification performance for BayesNet and Random Forest while degrading SVM accuracy. The findings highlight the significance of feature selection in classification.

While effective, the study does not go into detail on I2P's encryption techniques or the effects of various traffic characteristics on classification. Future research could overcome these constraints and investigate new detection methods for reliable I2P traffic identification.

# Paper 10

**Title**: Intrusion Traffic Detection and Characterization using Deep Image Learning.  
**Method:**Convolutional Neural Network (CNN)-based deep image learning with feature selection and 2D picture modification.  
**Dataset**:The CICIDS2017 and CSE-CIC-IDS2018 databases feature a variety of intrusion types and benign traffic.  
**Result**: On the CICIDS2017 and CSE-CIC-IDS2018 datasets, we achieved 99% and 97.5% accuracy, respectively.  
**Limitations**: Limited investigation of different deep learning models and difficulties in handling small attack sample numbers in datasets.

**Dataset Description**:   
The study employed the publicly accessible CICIDS2017 and CSE-CIC-IDS2018 databases, which contain a variety of attack types. CICIDS2017 contains 2,830,728 records, including 2,273,097 benign and 557,631 attack samples collected over five days. CSE-CIC-IDS2018 contains 16,232,943 records, including 13,484,708 benign and 2,748,235 attack samples, collected over ten days. Both datasets cover a variety of threats, including DDoS, SQL injection, brute force, and port scanning. CICFlowMeter was used for feature extraction, and the initial set of 80 features was decreased to 64 for model input utilising feature selection techniques.

**Method Description**:

1. Feature Selection: A ranking system examined 80 traffic features to choose the 64 most important ones for each dataset. These attributes were utilised to generate two-dimensional gray-scale pictures for CNN processing.  
2. Deep Image Learning Models: The CNN model extracts features using convolutional and max-pooling layers before classifying them with dense layers. To avoid overfitting, the model's design incorporates dropout layers, and softmax activation is used for multi-class output.

**Result Description**:  
The model achieved remarkable accuracy, with 99% for CICIDS2017 and 97.5% for CSE-CIC-IDS2018. Evaluation measures including precision, recall, and F1-score demonstrated its usefulness, particularly for DDoS attacks, which had the highest classification accuracy across both datasets. The confusion matrices demonstrated a low misinterpretation rate, with the exception of specific attack types such as penetration, where similarities to benign traffic posed issues. Overall, the findings verify the model's capacity to reliably classify intrusion types.

**Total Paper Summary:**

The paper, "Intrusion Traffic Detection and Characterisation Using Deep Image Learning," discusses the growing threat of cyber-attacks and the vital function of intrusion detection systems (IDS). It presents a novel image-based deep neural network model that uses convolutional neural networks (CNNs) to classify and characterise various incursion types. Using two datasets, CICIDS2017 and CSE-CIC-IDS2018, which include various attack scenarios, the model exhibits its power to achieve high classification accuracy of 99% and 97.5%, respectively.

The process consists of selecting characteristics with CICFlowMeter, extracting relevant network traffic features, and transforming them into two-dimensional greyscale images. These photos are processed using the CNN architecture to ensure accurate categorisation. The research emphasises the model's efficiency in managing datasets with various intrusion kinds, producing better results than standard methods.

Experimental evaluations support the model's effectiveness, with good precision and recall for the majority of assault types. The investigation emphasises CNNs' usefulness for intrusion detection due to their capacity to automatically identify critical features and perform fast computations. Future study will investigate alternative deep learning models, such as RNNs and LSTMs, for comparative analysis and further performance enhancements.

# Paper 11

**Title**:Large-Scale Network Traffic Monitoring with DBStream, a System for Rolling Big Data Analysis.  
**Method**: DBStream employs a Continuous Execution Language (CEL), a SQL-based declarative interface for expressing rolling data analysis using incremental queries.  
**Dataset**:Real-world network traffic data gathered from an Internet Service Provider (ISP) network using Tstat. Four vantage points were observed for five days, resulting in about 640 GB of TCP traffic data.  
**Result**:DBStream performed better than Spark, with a single DBStream node surpassing a cluster of 10 Spark nodes in rolling network analytics.  
**Limitations**:Scalability is hampered by its single-node architecture. The lack of integration with parallel database engines limits large-scale implementation.  
**Dataset Description**:   
The dataset was gathered over five days from four network vantage points in a live ISP network. Each vantage point recorded TCP traffic data, generating hourly text log files using Tstat. These logs contain more than 100 network indices, including round-trip time (RTT), uploaded/downloaded bytes, and unique IP addresses. The overall dataset volume is 640 GB, which is roughly twice the memory available throughout the cluster.  
**Method Description**:

1. DBStream is based on PostgreSQL and functions as a Data Stream Warehouse. It supports:  
2. The declarative Continuous Execution Language (CEL) allows for incremental query processing, enabling rolling analytics by mixing new data with previously computed results.  
3. Efficient window-based query execution, enabling for calculations such as moving averages, aggregations, and tracking state transitions (for example, active IP sets) over sliding time frames.  
4. Compatibility with SQL queries for integration with current systems. DBStream uses non-volatile storage to provide historical data access, allowing for both real-time and retrospective analytics.

**Result Description**:  
DBStream outperformed Spark for both incremental and rolling queries. For example, DBStream handled duties such as tracking separate active IP addresses in rolling windows faster than Spark's cluster.  
DBStream demonstrated near-linear scalability for a single-node system, efficiently processing data from up to four view points.Spark failed with incremental workloads needing frequent state updates (for example, changing different IPs every minute), due to synchronisation overhead.  
penetration, where similarities to benign traffic posed issues. Overall, the findings verify the model's capacity to reliably classify intrusion types.

**Total Paper Summary:**

The study "Large-scale Network Traffic Monitoring with DBStream, a System for Rolling Big Data Analysis" discusses the issues of processing high-speed, heterogeneous network data. It presents DBStream, a SQL-based system that is intended for incremental data analysis, specifically rolling updates to statistical reports over continuous data streams. DBStream functions as a Data Stream Warehouse, capable of processing and storing massive amounts of network traffic data while providing both real-time and historical analysis.

The Continuous Execution Language (CEL) is a key component of DBStream, allowing users to declaratively build rolling analytics using SQL. CEL supports incremental queries, which update results more efficiently by merging new data into previous outputs rather than recalculating from scratch. This functionality is shown through use cases such as rolling averages and monitoring active IP addresses over time.

The research also compares the performance of DBStream and Spark, a prominent parallel processing tool. Experimental results show that a single DBStream node can beat a ten-node Spark cluster for rolling analytics jobs due to DBStream's optimised incremental processing.

Finally, DBStream provides a scalable and effective option for putting out big data analytics. Future work entails improving DBStream's scalability and incorporating powerful machine learning capabilities for complicated analytics.

# Paper 12

**Title**: Malware Traffic Detection Using Tamper-Resistant Features.  
**Method**: Unsupervised anomaly detection employs tamper-resistant transport layer features collected from TCP flows.  
**Dataset**: Public datasets for normal traffic (University of Twente) and malware traffic (21 malware variants).  
**Result**: The system effectively detects Command and Control (C2) heartbeat traffic, with high AUC scores across several methods.  
**Limitations**: Newer malware families reduce detection performance by mimicking legal HTTP traffic, resulting in false negatives.

**Dataset Description**:   
The study utilises two primary datasets:

1. Legitimate Traffic: Public network traces acquired by the University of Twente in a controlled setting comprising internal/external traffic of a small-scale organisation. The dataset comprises a variety of protocols, including HTTP, SMTP, and IMAP, which depict typical enterprise network behaviour.  
2. Malware Traffic: Publicly available traces from 21 malware families, including Agobot, Zeus, Kelihos, and others, captured between 2007 and 2014\. The malware dataset contains approximately 3,600 flows, primarily TCP-based C2 heartbeat communication. Each flow illustrates a distinct malicious behaviour, such as spam dissemination, DDoS, and command updates.  
   

**Method Description**:  
The framework employs transport layer features derived from the first five packets of a TCP flow following a three-way handshake. The features are intended to be tamper-resistant, avoiding payload, port-based, or flag-based data, which are prone to evasion strategies such as encryption or changing port numbers.  
Key steps include:

1. Feature Extraction: Extract 248 flow-level features and use correlation-based filtering to uncover discriminative features such flow time, payload size, RTT, and goodput.  
2. Calibration: Change time-sensitive features (such as RTT) to reduce differences between synthetic virus trails and real-world network traffic.  
3. Detection algorithms: To find anomalies in blended malware and legitimate communication, use four anomaly detection algorithms: OCSVM, k-NN, LSAD, and k-Means.  
   

**Result Description**:  
High Detection Accuracy: k-NN outperformed other approaches in detecting abnormalities, with AUC scores frequently above 0.95 for malware families like DonBot and Kelihos.

**Total Paper Summary:**

The paper "Malware Traffic Detection Using Tamper-Resistant Features" introduces a new methodology for detecting malware communication based on robust transport-layer features. This strategy overcomes the shortcomings of existing systems, which frequently rely on readily faked or encrypted characteristics, making them susceptible to evasion by sophisticated malware.

The methodology extracts tamper-resistant properties from the first few TCP packets sent between endpoints, focussing on malware heartbeat traffic—communication required for command-and-control (C2) operations. By avoiding payload inspection and relying on statistical flow aspects, the method reduces privacy concerns while remaining successful on high-speed networks.

Real-world datasets representing various malware families were used in the evaluations. The system exhibited the ability to discriminate between genuine and malicious C2 communication, even when malware used traffic-shaping techniques to mimic lawful behaviour. The study also examined other anomaly detection algorithms, finding that k-nearest neighbours (k-NN) outperformed the others. However, issues remain with emerging malware families that obscure their communication patterns within HTTP traffic, resulting in lower detection rates.

The research emphasises the relevance of tamper-resistant features and supplementary diagnostics for reducing false negatives. Future research proposes incorporating new data sources, such as DNS characteristics, to improve detection skills and reduce false positives in developing network settings.

# 

# Complete Table

| S.no | Year | Title | Method | Dataset | Result | Limitations |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 2017 | Tor Traffic Analysis and Detection via Machine Learning Techniques | Machine learning techniques, leveraging network-based features, to detect and classify Tor traffic. | Real-world network traffic captured using tools like Wireshark, including Tor and non-Tor traffic. | The proposed methods achieved a high precision of 1.0 using the jRip algorithm for Tor traffic classification. |  Limited exploration of application environments beyond the evaluated scenarios, such as cloud platforms. |
| 2 | 2023 | Machine Learning Based Classification of IoT Traffic | Comparison of 4 ML algorithms and 3 NNs under different undersampling strategies. | IoTID20 dataset with 625,783 instances of normal and anomalous traffic in a smart home setup. | XGBoost achieved near-perfect accuracy and outperformed other models under data reduction scenarios; NNs underperformed with reduced training data. |  Simulated dataset; requires validation on real-world data and extension to multiclass classification. |
| 3 | 2024 | IoT Network Traffic Analysis with Deep Learning | Ensemble model combining CNN+LSTM and Random Forest with pre-trained KNN. | KDD Cup 1999 dataset (10%), 494,021 entries, simulated military network data. | The ensemble model achieved 98.22% accuracy, outperforming AutoEncoder and GAN models in anomaly detection. | Dataset is outdated and simulated; future work requires testing on real-world IoT datasets. |
| 4 | 2024 | Design of an Efficient Forensic Layer for IoT Network Traffic Analysis Engine Using Deep Packet Inspection via Recurrent Neural Networks | Deep packet inspection with LSTM and GRU-based RNNs for IoT attack detection. | IoT-23, CICIDS2017, IoT-Traffic, and UNSW-NB15 datasets combined into 900,000 records. | Achieved 98.3% accuracy, 97.5% precision, and 98.9% recall, surpassing ADGCN, LDNN, and FDRL in precision, recall, and delay metrics. | Limited scalability and real-world validation; requires optimization for resource-constrained IoT devices. |
| 5 | 2018 | IoT Devices Recognition Through Network Traffic Analysis | Random Forest and five other classifiers analyze bidirectional flows for IoT device recognition. | 7-day smart home traffic data from four IoT devices (3222 training, 805 testing flows).  | Random Forest achieved 99.9% accuracy. | Dataset limited to four devices; scalability to larger, diverse networks is unexplored. |
| 6 | 2012 | Detecting Malicious Websites by Learning IP Address Features | Machine learning using IP address-based features; evaluated with SVM classifiers. | IP data from Alexa’s top 10,000 websites, MDL, and campus network traffic. | 90.2% accuracy, 99.4% AUC; effective for unknown IPs. | False positives from benign hosting services; limited scalability to larger datasets. |
| 7 | 2023 | Network Anomaly Detection Through IP Traffic Analysis With Variable Granularity | The Fast xFlow Proxy is used to decompose traffic and discover anomalies based on correlation.  | Synthetic traffic datasets that model large-scale IP network behaviours and anomalies. | Accurately detects large-scale abnormalities (\~100%) and smaller changes (80-90%), even in noisy conditions. | Relies on synthetic data; lacks real-world validation and the capacity to pinpoint anomalous sources. |
| 8 | 2010 | A Real-Time DDoS Attack Detection and Prevention System Based on Per-IP Traffic Behavioral Analysis | Per-IP behavioural analysis using a non-parametric CUSUM algorithm.  | Network traffic data from a university network.  | SYN flooding attacks were detected with great accuracy and a negligible computational overhead. | Limited scalability testing; efficacy is dependent on the deployment environment.  |
| 9 | 2019 | I2P Anonymous Traffic Detection and Identification | Detection and classification with NaiveBayes, BayesNet, SVM, and RandomForest  | I2P traffic data was gathered using Wireshark and RouterInfo.  | RandomForest obtained 100% classification accuracy through excellent feature selection. | The analysis of encryption techniques and the impact of feature selection is limited; it focusses on only four algorithms. |
| 10 | 2020 | Intrusion Traffic Detection and Characterization using Deep Image Learning | CNN-based deep image learning includes feature selection and 2D picture modification.  | CICIDS2017 (2.8 million records); CSE-CIC-IDS2018 (16 million records). | CICIDS2017 achieved 99% accuracy, whereas CSE-CIC-IDS2018 achieved 97.5%.  | Challenges include modest attack sample numbers and little investigation of various deep learning models. |
| 11 | 2023 | Large-Scale Network Traffic Monitoring with DBStream | Incremental rolling data analysis using a declarative Continuous Execution Language (CEL) in DBStream. | Real-world ISP traffic logs (640 GB) obtained over five days with Tstat.  | Outperformed Spark uses rolling data analysis to efficiently analyse many viewpoint points on a single DBStream node. | Scalability is constrained by the single-node architecture and the lack of integration with parallel database engines. |
| 12 | 2015 | Malware Traffic Detection Using Tamper-Resistant Features | Unsupervised anomaly detection with tamper-resistant transport layer features derived from TCP traffic.  | Public datasets include University of Twente network traffic and malware traffic from 21 malware families. | Detects C2 malware heartbeat traffic with good AUC scores using k-NN, resulting in robust detection of both known and stealth malware.  | Detection performance for recent malware families decreases owing to imitation of normal HTTP traffic.  |

