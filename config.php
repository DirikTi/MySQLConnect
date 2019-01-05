<?php

class Configuration
{
	function __construct($host, $user, $password, $db)
	{
		$this -> host = $host;
		$this -> db = $db;
		$this -> password = $password;
        $this -> user = $user;
	}

	public function connectMySQL()
	{
        if($con =mysqli_connect($this->host, $this->user, $this->password, $this->db))
            $this -> con = $con;
			return $con;
		die("Failed to connect to MySQL: ".mysqli_connect_error());
    }

	public function connectPDO()
	{
		try{
			$dbh = new PDO('mysql:host=$host;dbname=$db', $user, $password);
			$dbh -> setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			return True;
		}
		catch (PDOException $e){
			echo "ERROR CONNECTİON FAILED: ". $e->getMessage();
		}
	}

    //Select Data from mysqlDatabase;
	public function mysqlSelectData($sql)
	{
        $con = $this->con;
        
        if($con == null){
            return "ERROR: not connected,  you need to use connectMySQL fucntion";
        }
        $result = $con -> query($sql);
        $number = $result ->num_rows;
		if($number > 0)
		{
            //$row equal please;
            
            $results = [
		    'num_rows' => $number,
		    'row'=>$result->fetch_assoc()
	    ];
			return  $results;
		}
		else
		{
			return false;
		}
	}

	public function mysqlRead($sql)
	{
        $con = $this->con;
        if($con == null){
            return "ERROR: not connected,  you need to use connectMySQL fucntion";
        }else{
            return $con -> query($sql);
        }
		
	}

	public function PDOSelectData($sql)
	{
        $con = $this->con;
		try {
			$stmt = $con -> query($sql);
			return $stmt -> fetch();	
		} 
		catch (PDOException $e) {
			echo "Select Data sql: ".$sql. "<br>".$e->getMessage();
		}
	}

	public function PDOReadSql()
	{
        $con = $this->con;
		try{
			$con -> exec($sql);
		}
		catch (PDOException $e){
			echo "sql: ".$sql. "<br>".$e->getMessage();
        }
        
        $con->close();
	}
	
	//DIE CONNECT..
	public function closeConnect()
	{
        $con = $this->con;
		$conn -> close();
	}
}
?>
