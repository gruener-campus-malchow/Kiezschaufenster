<?php
	$ads = [];

	$server = "localhost";
	$user = "ksf_server";
	$password = "passwort";
	
	$conn = new mysqli($server, $user, $password);
	$conn->query("USE ksf_server;");
	$sql = 'SELECT * FROM werbungen';
	$result = $conn->query($sql);
	
	if ($result->num_rows > 0) {
		while($row = $result->fetch_assoc()) {
			$ads[] = [
				"id"	=>	$row["id"],
				"html"	=>	addslashes($row["html"]),
				"time"	=>	$row["time"]
			];
		}
	}

	echo(json_encode($ads));
?>