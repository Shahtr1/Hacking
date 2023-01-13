# Splunk

> Shahrukh Tramboo | March 25th, 2022

--------------------------------------

**Splunk**
Splunk is used for monitoring and searching through big data. It indexes and correlates information in a container that makes it searchable, and makes it possible to generate alerts, reports and visualizations.

**Components**
In a single instance, there are 3
1.	Forwarders
	Responsible for collecting data and forwarding it to another splunk instance. In here it would be indexer.


2.	Indexers/Peer Nodes
	Indexer is where data is being stored. But we cant straightaway use this data here.



3.	Search Heads/Cluster Members
	We use search heads, which inturn access the data which is present in indexer and lets us do the analysis or visualization or reporting, gives you alerts etc



There are other components which manage the above components, these comes with concept of distributive deployment.
1.	Deployment Server
	Any changes that of data from source to destination, those updates are coming from deployment server and brought into forwarders.


2.	Cluster Master
	Monitors the Indexes or Peer Nodes
	Makes sure are Peers are up, no downtime, no data replication
	It also manages search heads, tells the seacrh head where to look the data, which index to access to get the data


3.	Deployer
	Responsible for making sure, that any updates to config, or operations, all those things are sent to clusters(Search Head)

