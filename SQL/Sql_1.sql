CREATE DATABASE BigTaxi;

USE BigTaxi;

CREATE TABLE Users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL UNIQUE,
    gmail VARCHAR(255) NOT NULL UNIQUE,
    password1 VARCHAR(255) NOT NULL,
    password2 VARCHAR(255) NOT NULL,
    CHECK (password1 = password2)
);

CREATE TABLE DriverProfile(
	id INT PRIMARY KEY AUTO_INCREMENT,
    u_id INT,
    User_Id VARCHAR(255) UNIQUE,
    Full_Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Mobile_No VARCHAR(255) NOT NUll,
    TaxiName VARCHAR(255) NOT NULL,
    TaxiPagangerLimit VARCHAR(20) NOT NULL,
    Taxi_Type VARCHAR(255) DEFAULT('Small Taxi'),
    CONSTRAINT Dp FOREIGN KEY (u_id) REFERENCES Users(id)
);

-- check for luxery aur normal card column, and Status Of Driver (activate or not)
ALTER TABLE DriverProfile
ADD COLUMN TaxiCondition VARCHAR(255) DEFAULT('normal'),
ADD COLUMN DriverStatus VARCHAR(255) DEFAULT('Activte'),
ADD COLUMN Gender VARCHAR(20) DEFAULT('MALE'),
ADD COLUMN Age VARCHAR(5) NOT NULL,
ADD COLUMN State VARCHAR(255) NOT NULL,
ADD COLUMN City VARCHAR(255) NOT NULL,
ADD COLUMN PinCode VARCHAR(255) NOT NULL;

CREATE TABLE TravelersProfile(
	id INT PRIMARY KEY AUTO_INCREMENT,
    p_id INT,
    Profile_Id VARCHAR(255) UNIQUE,
    Full_Name VARCHAR(255) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Mobile_No VARCHAR(255) NOT NULL,
    PinCode VARCHAR(10) NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    Age VARCHAR(5) NOT NULL,
    CONSTRAINT Tp FOREIGN KEY (p_id) REFERENCES Users(id)
);

ALTER TABLE TravelersProfile
ADD COLUMN RefrelCodeOfDriver VARCHAR(255);

SELECT * FROM Users;
SELECT * FROM DriverProfile;
SELECT * FROM TravelersProfile;


-- 12656

CREATE TABLE TaxiAvailable(
	id INT PRIMARY KEY AUTO_INCREMENT,
    TaxiAva_id VARCHAR(100) NOT NULL UNIQUE,
    State VARCHAR(255) NOT NULL,
	City VARCHAR(255) NOT NULL,
    DiverId INT,
    Pincode VARCHAR(100) NOT NULL,
    CONSTRAINT D_Id FOREIGN KEY (DiverId) REFERENCES TravelersProfile(id)
);

CREATE TABLE OnRunningTaxi(
	id INT PRIMARY KEY AUTO_INCREMENT,
	ORT_Id VARCHAR(255) NOT NULL UNIQUE,
	Driver_Id INT,
    Traveler_Id INT,
    Location VARCHAR(255) NOT NULL,
	FairPrice VARCHAR(20) NOT NULL,
    StartTaxi VARCHAR(50) NOT NULL,
    -- diver will input 
    EndTime VARCHAR(50) NOT NULL
);

CREATE TABLE OrderUser(
	id INT PRIMARY KEY AUTO_INCREMENT,
    Ord_Id VARCHAR(255) NOT NULL UNIQUE,
    User_Id INT,
    AddressFrom VARCHAR(255) NOT NULL, 
    AddressTo VARCHAR(255) NOT NULL,
    Pincode VARCHAR(200),
    Ord_Time VARCHAR(255),
    Ord_Status VARCHAR(255) DEFAULT('Activate'),
    CONSTRAINT Ord FOREIGN KEY (User_Id) REFERENCES TravelersProfile(id)
);

DROP TABLE OrderUser;

CREATE TABLE OrdDone(
	id INT PRIMARY KEY AUTO_INCREMENT,
    Ord_Done_Id VARCHAR(255) NOT NULL UNIQUE,
    Order_id INT,
    Review VARCHAR(255) NOT NULL,
    Rating INT DEFAULT(1),
    CONSTRAINT Ords_Done FOREIGN KEY (Order_id) REFERENCES OrderUser(id)
);

CREATE TABLE CancelOnRunning(
	id INT PRIMARY KEY AUTO_INCREMENT,
    COR_ID VARCHAR(255) NOT NULL UNIQUE,
    -- will by defult, that come from template, USER_ID
    CHECK_HOW_CANCEL VARCHAR(255) NOT NULL,
    -- Driver ID 
    Driver_ID VARCHAR(255) NOT NULL,
    -- by default
    PlaceWhereLeft VARCHAR(255) NOT NULL,
    -- by default use any thing
    KiloMeter VARCHAR(255) NOT NULL,
    Review VARCHAR(255) NOT NULL
);

SHOW TABLES;

SELECT * FROM cancelonrunning;
SELECT * FROM driverprofile;
SELECT * FROM orddone;
SELECT * FROM orderuser;
SELECT * FROM taxiavailable;
SELECT * FROM travelersprofile;
SELECT * FROM users;