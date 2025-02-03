# Dataset \- 1

Dataset Link: https://www.kaggle.com/datasets/ziya07/iot-edge-processed-traffic-and-incident-dataset/data

Column Names with values or range

| column name | column description | column valuesor range |
| ----- | ----- | ----- |
| timestamp | The exact time when the data was recorded. | DateTime format (e.g., YYYY-MM-DD HH:MM:SS) |
| sensor\_id | A unique identifier for each vehicle sensor. | String (e.g., Vehicle\_1, Vehicle\_2) |
| vehicle\_speed (km/h) | Speed of the vehicle in kilometers per hour. | Numeric (e.g., 0–200 km/h) |
| latitude | GPS latitude of the vehicle's location. | Float (e.g., \-90.0 to 90.0) |
| longitude | GPS longitude of the vehicle's location. | Float (e.g., \-180.0 to 180.0) |
| traffic\_pattern | Traffic level at the time of recording. | Categorical (Light, Moderate, Heavy, Clear) |
| incident\_report | Type of incident occurring at the time. | Categorical (None, Accident, Breakdown, Traffic Jam, Police Blockade) |
| accident\_hotspot | Indicator if the location is a known accident hotspot. | Binary (0: No, 1: Yes) |
| event\_type | Categorizes the event based on the data. | Categorical (Normal, Accident, Congestion) |

Column to predict: event\_type

Dataset size (idi add for all): 28kb

   
Dataset description in detail: 

This dataset contains real-time data collected from IoT sensors deployed in an urban environment to enhance public management systems. Sensors record vehicle speed, GPS locations, road traffic patterns, and incident reports, which are processed at the network's edge to enable low-latency, real-time decision-making.

The dataset highlights:

* Vehicle behavior through speed and location data.  
* Patterns of congestion, accidents, and disruptions.  
* Identifying accident hotspots to mitigate risks.

Potential use cases include:

* Predictive traffic management systems.  
* Identifying areas prone to accidents for preventive measures.  
* Real-time traffic monitoring and optimization.

This data is essential for smart city applications aimed at improving traffic flow, reducing accident rates, and enhancing public service efficiency.

# Dataset \- 2

Dataset Link: https://www.kaggle.com/datasets/ravikumargattu/network-traffic-dataset?select=Midterm\_53\_group.csv

Column Names with values or range

| column name | column description | column valuesor range |
| ----- | ----- | ----- |
| Time | Timestamp of the network traffic instance. | Numeric, time in seconds (e.g., 0.000000, 1.169060) |
| Source | Source IP or MAC address of the traffic. | IPv4/IPv6 address or MAC address (e.g., 192.167.8.166) |
| No. | Number of the traffic instance. | Integer (e.g., 1, 2, 3). |
| Destination | Destination IP or MAC address of the traffic. | IPv4/IPv6 address or MAC address (e.g., 192.167.255.255) |
| Protocol | Protocol used by the instance.  | Categorical (e.g., NBNS, ARP) |
| Length | Length of the traffic instance in bytes. | Numeric (e.g., 60, 92\) |
| Info | Additional information about the traffic instance. | Textual description (e.g., "Name query NB WPAD\<00\>") |

Column to predict: ,   
**Protocol** (for classification tasks)  
**Info** (for anomaly detection or traffic pattern analysis)

Dataset size: 52.9mb

Dataset description in detail

This dataset comprises real-time network traffic data captured using Wireshark on a Kali machine at the University of Cincinnati. The capture was conducted over one hour, collecting 394,137 instances of network activity. The dataset is a rich source of information for machine learning applications in cybersecurity, providing details like source and destination IP addresses, protocol types, packet lengths, and timestamped traffic events.

The majority of the features are numeric, with some nominal (e.g., protocol) and textual (e.g., info) attributes. The dataset is especially suited for tasks such as:

* **Network Performance Monitoring**: Analyzing traffic patterns to improve network algorithms.  
* **Anomaly Detection**: Training models to identify irregular traffic patterns indicative of cyberattacks.  
* **Network Intrusion Detection**: Detecting malicious or anomalous traffic, including DoS attacks.

The inclusion of data from public, private, and enterprise networks ensures diverse scenarios for analysis, making this dataset invaluable for building robust machine learning models for cybersecurity applications.

# Dataset \- 3

Dataset Link: https://www.kaggle.com/datasets/vigneshvenkateswaran/bot-iot?select=data\_1.csv

Column Names with values or range

| column name | column description | column valuesor range |
| ----- | ----- | ----- |
| pkSeqID | Packet sequence identifier | Integer values starting from 1 |
| stime | Start time of the flow | Unix timestamp (floating-point) |
| flgs | Flags related to the packet | Nominal values such as "e" |
| proto | Protocol used in communication | Nominal values like "tcp," "udp," "arp," etc |
| saddr | Source IP address | IPv4 addresses (e.g., "192.168.100.1") |
| sport | Source port number |  Integer values or null for protocols without ports |
| daddr | Destination IP address | IPv4 addresses (e.g., "192.168.100.3") |
| dport | Destination port number | Integer values or null for protocols without ports |
| pkts | Number of packets in the flow | Integer values |
| bytes | Total bytes transferred | Integer values |
| state |  State of the connection. | Nominal values like "CON". |
| ltime | Last time the flow was seen. | Unix timestamp (floating-point). |
| seq | Flow sequence number. | Integer values. |
| dur | Duration of the flow. | Floating-point values in seconds. |
| mean | Mean of some calculated flow metrics. | Floating-point values. |
| stddev | Standard deviation of flow metrics. | Floating-point values. |
| smac | Source MAC address. | Nominal values (e.g., "00:00:00:00:00:00"). |
| dmac | Destination MAC address. | Nominal values (e.g., "FF:FF:FF:FF:FF:FF"). |
| sum | Summation of flow metrics. | Floating-point values.  |
| min | Minimum of some calculated flow metrics. | Floating-point values.  |
| max | Maximum of some calculated flow metrics. | Floating-point values. |
| soui | Source organization unique identifier. | Integer values. |
| doui | Destination organization unique identifier | Integer values. |
| sco | Source country code. | Integer values. |
| dco | Destination country code. | Integer values. |
| spkts | Number of source packets. | Integer values. |
| dpkts | Number of destination packets. | Integer values. |
| sbytes | Bytes sent from the source. | Integer values. |
| dbytes | Bytes sent to the destination. | Integer values. |
| rate | Packet rate. | Floating-point values. |
| srate | Source packet rate. | Floating-point values. |
| drate | Destination packet rate. | Floating-point values. |
| attack | Indicates if an attack is present. | Integer values (e.g., 0 for Normal, 1 for Attack). |
| category | Attack category.  |  Nominal values (e.g., "Normal", "DDoS"). |
| subcategory | Attack subcategory. | Nominal values (e.g., "Normal", "UDP Flood"). |

Column name to predict: attack 

Dataset size: 208mb

Dataset description in detail:

The BoT-IoT dataset was developed in the Cyber Range Lab of UNSW Canberra and features a mix of normal and botnet traffic. It is highly realistic and tailored for research in IoT network forensics. It contains traffic data for multiple attack types, including DDoS, DoS, keylogging, and data exfiltration. The dataset spans over 72 million records, reduced to 3 million for ease of handling in research applications. With detailed flow metrics, this dataset supports advanced analysis for cybersecurity and IoT applications, such as intrusion detection and anomaly detection.

# Dataset \- 4

Dataset Link: https://www.kaggle.com/datasets/dhoogla/unswnb15?select=UNSW\_NB15\_training-set.parquet

Column Names with values or range

| column name | column description | column valuesor range |
| ----- | ----- | ----- |
| pkSeqID | Packet sequence ID, unique identifier for each entry. | Integer values starting from 1\. |
| stime | Start time of the packet | Floating-point UNIX timestamps |
| flgs | Flags associated with the packet | String (e.g., 'e') |
| proto |  Protocol used in the communication (e.g., TCP, UDP) | Categorical |
| saddr | Source IP address | String (e.g., '192.168.100.1') |
| sport | Source port number | Integer (or null for certain protocols like ARP) |
| daddr | Destination IP address | String (e.g., '192.168.100.3') |
| dport | Destination port number | Integer (or null for certain protocols like ARP) |
| pkts | Number of packets in the flow | Integer values |
| bytes | Total number of bytes in the flow | Integer values |
| state | Connection state | String (e.g., 'CON') |
| ltime | Last time the connection was active | Floating-point UNIX timestamps |
| seq | Flow sequence number |  Integer values |
| dur |  Duration of the connection | Floating-point values |
| mean, stddev, sum, min, max | Statistical metrics of the flow's characteristics | Floating-point values |
| smac, dmac | Source and destination MAC addresses | String (e.g., '00:11:22:33:44:55') |
| sco, dco | Source and destination country | String values |
| spkts, dpkts | Number of packets sent and received | Integer values |
| sbytes, dbytes | Bytes sent and received | Integer values |
| rate, srate, drate | Flow rates (total, source, and destination) | Floating-point values |
| attack | Indicates whether the flow is an attack | Binary (0 \= Normal, 1 \= Attack) |
| category, subcategory | Attack category and subcategory | Strings (e.g., 'Normal', 'DoS') |

Column to predict: attack(Binary target variable indicating attack presence (1) or normal traffic (0)

Dataset size: 26.7mb

Dataset description in detail:

The BoT-IoT dataset was generated in a controlled, realistic network environment at the Cyber Range Lab of UNSW Canberra. The network included both normal and botnet traffic with various attack categories, such as DDoS, DoS, OS and Service Scan, Keylogging, and Data Exfiltration. It comprises 72 million records in pcap format, reduced to a more manageable size in CSV format (16.7 GB). Additionally, a smaller subset (5%) containing 3 million records was extracted for easier handling. This subset is divided into four files totaling 1.07 GB. The dataset is extensively labeled, offering high granularity for network traffic analysis, including attack and normal traffic categorization. Key features include packet-level statistics, connection states, MAC addresses, and protocol-based metrics, making it highly suitable for intrusion detection research and ML-based model training.

# Dataset \- 5

Dataset Link: https://www.kaggle.com/datasets/astralfate/iot23-dataset?select=iot23\_combined.csv

Column Names with values or range

| column name | column description | column valuesor range |
| ----- | ----- | ----- |
| ts | Timestamp indicating the start of the connection. | Floating-point UNIX timestamps. |
| id.orig\_h | Originating IP address. | String (e.g., '192.168.1.132'). |
| duration | Duration of the connection. | Floating-point values in seconds. |
| orig\_bytes | Bytes sent by the originator. | Integer values (e.g., 0, 48). |
| resp\_bytes | Bytes received by the originator. | Integer values (e.g., 0, 311). |
| missed\_bytes | Bytes that were missed during transmission. | Floating-point values (e.g., 0.0). |
| orig\_pkts | Packets sent by the originator. | Floating-point values (e.g., 1.0, 5.0). |
| orig\_ip\_bytes | Total IP bytes sent by the originator. | Floating-point values (e.g., 62.0, 16416.0). |
| resp\_pkts  | Packets received by the originator. | Floating-point values (e.g., 0.0, 1.0). |
| resp\_ip\_bytes | Total IP bytes received by the originator. | Floating-point values (e.g., 0.0, 339.0) |
| label | Classification label indicating whether the connection is benign or malicious. | Categorical (e.g., 'Benign', 'Malicious'). |
| proto\_icmp, proto\_tcp, proto\_udp | Protocol indicators for ICMP, TCP, and UDP traffic. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_OTH | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes). |
| conn\_state\_REJ | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_RSTO | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes). |
| conn\_state\_RSTOS0 | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_RSTR | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_RSTRH | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_S0 | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_S1 | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes). |
| conn\_state\_S2 | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_S3 | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_SF | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
| conn\_state\_SH | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes).  |
|  conn\_state\_SHR | Connection states describing various states of the connection. | Binary (0 \= No, 1 \= Yes). |

Column to predict: label

Dataset size: 163mb

Dataset description in detail:

The IoT-23 dataset consists of labeled network traffic collected from IoT devices to analyze benign and malicious behaviors. It was generated at the Stratosphere Laboratory and includes 20 scenarios of IoT network traffic, with both normal device usage and traffic generated by malware. This dataset contains various features like connection timestamps, packet sizes, IP and MAC information, and connection state indicators. Its labeling makes it suitable for supervised machine learning tasks such as intrusion detection or anomaly detection in IoT environments.

The `iot23_combined.csv` file is a consolidated version of the dataset with cleaned and minimalistic features, designed for lightweight analysis and machine learning experimentation. Each row represents a connection record, with features covering the connection's attributes, states, and protocols, alongside its label for classification.

# Dataset \- 6

Dataset Link   
https://www.kaggle.com/datasets/malqarni/iotdataset?resource=download

Column Names with values or range

| column name | column description | column valuesor range |
| ----- | ----- | ----- |
| Timestamp |  The time the packet was captured  | DateTime format (e.g., YYYY-MM-DD HH:MM:SS) |
| Source IP | IP address of the source device in the network | IPv4/IPv6 addresses (e.g., 192.168.1.1) |
| Destination IP | IP address of the target device |  IPv4/IPv6 addresses (e.g., 192.168.1.2)  |
| Source Port | Source port of the packet | Integer (e.g., 0–65535) |
| Destination Port | Target port of the packet | Integer (e.g., 0–65535) |
| Protocol | Protocol used by the packet (e.g., TCP, UDP) | String (e.g., TCP, UDP) |
| Flow Duration | Duration of the data flow | Integer (e.g., milliseconds) |
| Total Forward Packets | Total number of packets sent forward in the flow | Integer (e.g., 0–65535) |
| Total Backward Packets | Total number of packets sent backward in the flow | Integer (e.g., 0–65535) |

Column to predict:- traffic,flow\_Duration,Pkt\_Len\_Mean

Dataset size:- 104.7 MB

Dataset description in detail:-

                   The dataset appears to be a network traffic dataset designed for intrusion detection, focusing on analyzing and classifying network flow data. Each row in the dataset represents a network flow, characterized by various features capturing its behavior. Key columns include **`Flow_Duration`**, representing the duration of a flow in microseconds, and **`Tot_Fwd_Pkts`** and **`Tot_Bwd_Pkts`**, which detail the total number of packets transmitted in forward and backward directions, respectively. 

                    The dataset also includes features such as **`Pkt_Len_Mean`**, the average packet length, and **`Fwd_Pkt_Len_Max`** and **`Bwd_Pkt_Len_Max`**, which record the maximum packet lengths in forward and backward directions. Additionally, **`Flow_Byts/s`** and **`Flow_Pkts/s`** provide measures of flow throughput in bytes and packets per second. A critical column, **`Normal`**, indicates whether the flow is normal or anomalous, making it a target variable for intrusion detection tasks. Other features like **`Fwd_Pkts/s`**, **`Bwd_Pkts/s`**, and **`Pkt_Len_Std`** add depth to the analysis, capturing statistical and temporal characteristics of the flow. This dataset is well-suited for tasks such as anomaly detection, classification of normal and abnormal traffic, or predicting specific characteristics of network flows.

# Dataset \- 7

Dataset Link   
[https://drive.google.com/file/d/1ruY3FLogaIG8ZW4RK5lxep6IcgRTXElA/view?usp=drivesdk](https://drive.google.com/file/d/1ruY3FLogaIG8ZW4RK5lxep6IcgRTXElA/view?usp=drivesdk)

[https://www.kaggle.com/datasets/rohulaminlabid/iotid20-dataset](https://www.kaggle.com/datasets/rohulaminlabid/iotid20-dataset)

| Column Name | Description | Values/Range |
| ----- | ----- | ----- |
| Timestamp | The time the packet was captured | DateTime format (e.g., YYYY-MM-DD HH:MM:SS) |
| Source IP | IP address of the source device | IPv4/IPv6 addresses (e.g., 192.168.1.1) |
| Destination IP | IP address of the target device | IPv4/IPv6 addresses (e.g., 192.168.1.2) |
| Source Port | Source port of the packet | Integer (0–65535) |
| Destination Port | Destination port of the packet | Integer (0–65535) |
| Protocol | Protocol used in the network communication | Integer (e.g., 1 \= ICMP, 6 \= TCP, 17 \= UDP) |
| Flow Duration | Duration of the flow | Integer (e.g., 1–1,000,000 microseconds) |
| Total Forward Packets | Total number of packets sent forward | Integer (e.g., 1–10,000) |
| Total Backward Packets | Total number of packets sent backward | Integer (e.g., 1–10,000) |
| Forward Packet Length | Length of forward packets | Float (mean, max, min, std values) |
| Backward Packet Length | Length of backward packets | Float (mean, max, min, std values) |
| Flow Bytes per Second | Rate of bytes transmitted per second | Float (e.g., 0.0–1,000,000 bytes/s) |
| Flow Packets per Second | Rate of packets transmitted per second | Float (e.g., 0.0–1,000 packets/s) |
| Flags (e.g., SYN, ACK, FIN) | TCP flags captured in the flow | Binary/Integer (0, 1\) |
| Active/Idle Time | Active or idle durations of the flow | Float (mean, max, min, std values in microseconds) |
| Normal | Class label indicating normal vs anomalous | Binary (0 \= Normal, 1 \= Anomalous) |

Column to predict:-

* **Column Name**: Normal  
  * **Description**: Whether the flow is normal (0) or anomalous (1).

Dataset size:- 246 MB

Dataset description in detail:-

The dataset contains a comprehensive collection of network traffic data, including extensive flow-based features derived from packet-level analysis. It consists of 78 columns, each of which represents a specific property that defines network behaviour. These features include source and destination IP addresses, ports, protocols, flow durations, and packet statistics such as total number of forward and backward packets, packet lengths (minimum, maximum, mean, and standard deviation), and byte transfer rates.

Furthermore, the dataset includes time-based metrics such as flow inter-arrival times and active/idle durations, which provide information about the temporal dynamics of network communication. Flags such as SYN, ACK, and FIN are also recorded, showing TCP-specific behaviour. The dataset's numerical properties (such as flow bytes/packets per second) provide a detailed insight of network performance.

The target variable, Normal, is a binary classification label, with 0 representing normal traffic and 1 representing anomalous or potentially malicious communication. This dataset's wide range of attributes makes it perfect for training machine learning models to detect network anomalies, intrusions, and attacks. The dataset size, which might include millions of rows, ensures sufficient variation for creating effective predictive models while reflecting real-world network conditions.

# Dataset \- 8

Dataset Link :- [https://www.kaggle.com/datasets/jsrojas/ip-network-traffic-flows-labeled-with-87-apps](https://www.kaggle.com/datasets/jsrojas/ip-network-traffic-flows-labeled-with-87-apps)  
​​

| Column Name | Column Description | Values/Range |
| ----- | ----- | ----- |
| **Flow.ID** | Unique identifier for a network flow | Alphanumeric string (e.g., 172.19.1.46-10.200.7.7-52422-3128-6) |
| **Source.IP** | Source device's IP address | IPv4/IPv6 addresses (e.g., 192.168.1.1) |
| **Source.Port** | Source port of the connection | Integer (0–65535) |
| **Destination.IP** | Destination device's IP address | IPv4/IPv6 addresses (e.g., 10.200.7.7) |
| **Destination.Port** | Destination port of the connection | Integer (0–65535) |
| **Protocol** | Protocol used in the flow | Integer (e.g., 6 for TCP, 17 for UDP) |
| **Timestamp** | Timestamp of the flow | Datetime format (e.g., 26/04/2017 11:11:17) |
| **Flow.Duration** | Duration of the flow in microseconds | Integer (e.g., 0–2,000,000,000) |
| **Total.Fwd.Packets** | Total packets sent forward in the flow | Integer (0–10,000+) |
| **Total.Backward.Packets** | Total packets sent backward in the flow | Integer (0–10,000+) |
| **Total.Length.of.Fwd.Packets** | Total length of all forward packets in the flow | Integer (0–1,000,000+) |
| **Total.Length.of.Bwd.Packets** | Total length of all backward packets in the flow | Integer (0–1,000,000+) |
| **Fwd.Packet.Length.Max** | Maximum length of a single forward packet | Integer (0–65,535) |
| **Fwd.Packet.Length.Min** | Minimum length of a single forward packet | Integer (0–65,535) |
| **Fwd.Packet.Length.Mean** | Mean length of forward packets | Float (0–65,535) |
| **Fwd.Packet.Length.Std** | Standard deviation of forward packet lengths | Float (0–65,535) |
| **Bwd.Packet.Length.Max** | Maximum length of a single backward packet | Integer (0–65,535) |
| **Bwd.Packet.Length.Min** | Minimum length of a single backward packet | Integer (0–65,535) |
| **Bwd.Packet.Length.Mean** | Mean length of backward packets | Float (0–65,535) |
| **Bwd.Packet.Length.Std** | Standard deviation of backward packet lengths | Float (0–65,535) |
| **Flow.Bytes.s** | Number of bytes per second in the flow | Float (0–1 billion+) |
| **Flow.Packets.s** | Number of packets per second in the flow | Float (0–1 million+) |
| **Label** | Indicates whether the flow is benign or malicious | BENIGN, MALICIOUS |
| **L7Protocol** | Application layer protocol | Integer (e.g., 7 for HTTP, 91 for SSL) |
| **ProtocolName** | Name of the protocol | String (e.g., HTTP, SSL, HTTP\_PROXY) |

Column to predict:-  
Predict whether the network flow is BENIGN or MALICIOUS

Dataset size:- 1.77 GB

Dataset description in detail:-

The dataset includes a comprehensive collection of network flow statistics, which provides extensive insights into the traffic characteristics seen in a network environment. Each row represents a distinct flow, as indicated by attributes such as Flow ID, Source IP, Source Port, Destination IP, and Destination Port, providing for exact tracking of communication endpoints. The dataset collects both forward and backward traffic information, including the number and total length of packets transmitted in both directions, as well as metrics like maximum, minimum, mean, and standard deviation of packet lengths.

Temporal variables like as timestamps, flow durations, and inter-arrival times (IAT) provide a temporal understanding of the flows, allowing for the investigation of network activity patterns. Additionally, flow rates, indicated by metrics like as Flow Bytes/s and Flow Packets/s, aid in performance evaluation and anomaly discovery. Flags such as FIN, SYN, and ACK reveal session control information, whereas fields like Active Mean, Idle Mean, and Subflow Statistics characterise flows' behavioural patterns.

Labels such as BENIGN and protocol identifiers (e.g., HTTP\_PROXY, SSL) provide insights about flow classifications, which are critical for cybersecurity analysis. The dataset is rich in characteristics, making it ideal for machine learning models focused on traffic analysis, anomaly detection, and intrusion prevention.

# Dataset \- 9

Dataset Link:- https://www.kaggle.com/datasets/kimdaegyeom/5g-traffic-datasets/data

| Column Name | Description | Values or Range |
| ----- | ----- | ----- |
| Timestamp | The time the packet was captured | DateTime format (e.g., YYYY-MM-DD HH:MM:SS) |
| Source IP | IP address of the source device in the network | IPv4/IPv6 addresses (e.g., 192.168.1.1) |
| Destination IP | IP address of the target device | IPv4/IPv6 addresses (e.g., 192.168.1.2) |
| Source Port | Source port of the packet | Integer (e.g., 0–65535) |
| Destination Port | Destination port of the packet | Integer (e.g., 0–65535) |
| Protocol | The protocol used in the communication | TCP, UDP, ICMP, etc. |
| Length | The length of the packet | Integer (e.g., 0–1500 bytes) |
| Info | Additional information about the packet | Descriptions (e.g., SYN, ACK, data transfer, etc.) |
| Application | Type of application generating the traffic | Video Streaming, Live Streaming, Video Conferencing, etc. |
| Source Location | Location of the source device | Country, City, or GPS coordinates (if available) |
| Destination Location | Location of the destination device | Country, City, or GPS coordinates (if available) |
| Traffic Type | Type of traffic measured | OTT, Metaverse, Gaming, etc. |
| Data Size | Total size of captured data (if available) | Integer (e.g., in MB or GB) |
| Duration | Duration for which data was captured | Time in hours or minutes |

Column to predict:- detect anomalies,traffic types

Dataset size:- 3.2 GB

Dataset description in detail:-

The dataset is intended to collect network traffic statistics, which provides insights into the movement of information between devices across a network. Each entry in the dataset represents a single packet recorded during network traffic analysis, along with pertinent attributes that characterise the packet's path from source to destination. The timestamp, which reveals the exact time the packet was intercepted, and the source and destination IP addresses, which expose the communication's origin and destination, are two important columns. These IP addresses are generally IPv4 or IPv6 addresses that provide information about the involved devices.

The collection also includes information about the source and destination ports, which can be used to identify the individual application or service being used. The protocol field specifies the communication technique utilised, which could be TCP, UDP, or ICMP. The length of the packet is recorded, providing information on the extent of the data sent.

Additional columns detail the content and nature of the traffic, such as the info column, which indicates whether the packet is part of a handshake or a data transfer. Application categories like as video streaming, gaming, and video conferencing are identified, allowing traffic to be categorised depending on its use case. The dataset may also include the geographical locations of the source and destination devices, which provide extra context.

# Dataset \- 10

Dataset Link :-  
https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset?select=Friday-WorkingHours-Morning.pcap\_ISCX.csv

| Column Name | Column Description | Column Values or Range |
| ----- | ----- | ----- |
| Fwd Packet Length Max | Maximum length of the forwarded packets | Numeric values (e.g., 0.00 \- 1298.96, 1298.96 \- 2597.92, etc.) |
| Fwd Packet Length Min | Minimum length of the forwarded packets | Numeric values (e.g., 0.00 \- 1298.96, 1298.96 \- 2597.92, etc.) |
| Fwd Packet Length Mean | Mean length of the forwarded packets | Numeric values (e.g., 0.00 \- 1298.96, 1298.96 \- 2597.92, etc.) |
| Fwd Packet Length Std | Standard deviation of the forwarded packet lengths | Numeric values (e.g., 0.00 \- 1298.96, 1298.96 \- 2597.92, etc.) |
| Label | The label for classification or grouping | Categories (e.g., 0.00 \- 1298.96, 1298.96 \- 2597.92, etc.) |
| Source IP | IP address of the source device in the network | IPv4/IPv6 addresses (e.g., 192.168.1.1) |
| Destination IP | IP address of the target device | IPv4/IPv6 addresses (e.g., 192.168.1.2) |
| Source Port | Source port of the packet | Integer (e.g., 0–65535) |
| Destination Port | Destination port of the packet | Integer (e.g., 0–65535) |
| Timestamp | The time the packet was captured | DateTime format (e.g., YYYY-MM-DD HH:MM:SS) |

Column to predict:- Fwd Packet Length Max , Bwd Packet Length Mean

Dataset Size:- 16.2 MB

Dataset description in detail:-

The dataset you're working with appears to be focused on network traffic data, maybe for network intrusion detection or anomaly detection. It is likely to have a variety of attributes that indicate packet-level information collected from a network. These features include information about traffic patterns, packet statistics, and overall network performance, which can be utilised to identify odd or malicious activity.

Some frequent columns you may encounter are packet lengths (e.g., "Fwd Packet Length Mean," "Bwd Packet Length Max"), which provide information about the size of packets travelling via the network. Features such as "Flow Duration" and "Total Fwd Packets" reflect the length of a connection and the amount of data transported, respectively. These are critical for analysing traffic patterns and understanding the flow of data.

Additional columns may include flags (e.g., "Protocol Type," "Flag") that describe the packet's type (such as TCP, UDP, or other protocols). Other capabilities, such as "Timestamp" or "Source/Destination IP," provide contextual information about when and where the traffic originated and was routed, allowing you to trace specific network behaviour.

The target column you'd be predicting (for classification or regression) could be a defined category (such as attack vs. typical traffic) or a numerical measurement (such as network delay). The information can be used for developing models to detect security breaches or monitor network health.

