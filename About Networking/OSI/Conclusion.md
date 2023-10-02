# Process

Let's walk through the scenario of how you and your friend communicate using a computer network, considering all OSI model layers on both sides.

In this example, let's say you want to send your friend an email. Here's how it works:

## Sender's Side (Your Computer):

- ### Application Layer (Layer 7):

  You open your email client application (e.g., Outlook, Gmail).
  You compose an email message, including the text, attachments, and formatting.

- ### Presentation Layer (Layer 6):

  The Presentation Layer takes care of character encoding, ensuring that any special characters or symbols in your email are represented correctly.

- ### Session Layer (Layer 5):

  The Session Layer manages the communication session. In this case, it sets up a session for your email client to send data to your email provider's servers.

- ### Transport Layer (Layer 4):

  The Transport Layer takes the prepared email data and segments it into smaller packets for transmission. It adds source and destination port numbers.
  It decides whether to use TCP (for reliable, connection-oriented communication) or UDP (for faster, connectionless communication) based on the application's requirements.

- ### Network Layer (Layer 3):

  The Network Layer determines the best route for your email data to reach your email provider's servers. It adds source and destination IP addresses to each packet.

- ### Data Link Layer (Layer 2):

  The Data Link Layer manages how your computer accesses the physical network medium (e.g., Wi-Fi or Ethernet). It adds source and destination MAC addresses to the packets.

- ### Physical Layer (Layer 1):

  The Physical Layer handles the actual transmission of the data as electrical signals, radio waves, or whatever medium your network uses. The packets are sent over the physical network infrastructure to your router or network switch.

## Receiver's Side (Your Friend's Computer):

Now, let's consider how the data is processed on your friend's side.

- ### Physical Layer (Layer 1):

  The data packets containing your email travel over the physical network medium and reach your friend's router or network switch.

- ### Data Link Layer (Layer 2):

  The Data Link Layer on your friend's computer processes the incoming packets, checks if they are addressed to their device (using the destination MAC address), and passes them up to the Network Layer.

- ### Network Layer (Layer 3):

  The Network Layer on your friend's computer examines the destination IP address in the packets to determine if they are meant for their computer. If so, the packets are passed up to the Transport Layer.

- ### Transport Layer (Layer 4):

  The Transport Layer on your friend's computer reassembles the email data by combining the packets received. It checks for any missing or corrupted packets and, if necessary, requests retransmission.
  Once all data is received and verified, it passes the complete email data to the Session Layer.

- ### Session Layer (Layer 5):

  The Session Layer manages the communication session and ensures that the data is properly handed over to the Presentation Layer.

  Here's what the Session Layer does:

  - #### Session Establishment:
    When you start an application that requires network communication (e.g., a web browser or an email client), the Session Layer is responsible for setting up the session. This includes tasks like authentication and establishing session keys for security.
  - #### Dialog Control:
    The Session Layer helps in managing the orderly exchange of data between the devices. It defines who can send data and when. For example, in a video conference, it manages who has the right to speak at a given moment.
  - #### Synchronization:
    It ensures that data is correctly synchronized between sender and receiver. For instance, if you're watching a streaming video, the Session Layer helps ensure that the audio and video remain synchronized, preventing one from getting ahead of the other.

- ### Presentation Layer (Layer 6):

  The Presentation Layer on your friend's computer decodes any character encoding, decompresses data if it was compressed, and prepares the email content for display.

- ### Application Layer (Layer 7):

  Finally, the email client application running on your friend's computer receives the fully processed email data from the Presentation Layer. It displays the email, including text, attachments, and formatting, to your friend.
