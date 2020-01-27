4주차 Database Bootcamp
=========================

**목표** : Mysql을 이용하여 웹 크롤링으로 수집한 데이터를 Database화 한다. Entity-Relationship Modelling ERM 기법으로 데이터를 모델링하여 ERM 프로세스의 산출물을 가리켜 Entity-Relationship Diagram 즉, ERD로 데이터 모델을 그림으로 표현해보자. ERD는 개념적 데이터 모델 혹은 시맨틱 데이터 모델의 한 타입이다. 2020.01.23 ~ 2020.01.29

Courses
-------

### Database Bootcamp
- [DATABASE 1&2 - MySQL](https://www.inflearn.com/course/database-2-mysql-%EA%B0%95%EC%A2%8C), 생활코딩, 2018
- [SQL/DB(MySQL) 기본부터 파이썬/데이터분석 활용까지!](https://www.inflearn.com/course/SQL-DB-MYSQL-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B6%84%EC%84%9D), 인프런, 2019

### Theater Information Guide Database (MySQL)
- **Database create code**

```sql
CREATE DATABASE tig;
USE tig;

CREATE TABLE theaters(
    TheaterID int not null auto_increment,
    TheaterName int not null,
    Period varchar(50) not null,
    Place varchar(50) not null,
    OpeningDay date not null,
    ClosingDay date null,
    OpenRun boolean default null,
    primary key(TheaterID)
);

CREATE TABLE theaters_details(
    TheaterID int not null,
    ViewingAge varchar(50) null,
    PerformanceTime varchar(50) null,
    Descriptions varchar(255) null, 
    Price int null,
    Image blob null,
    ShopTitle varchar(50) null,
    ShopLink varchar(255) null,
    foreign key(TheaterID)
      references theaters(TheaterID) on delete cascade on update cascade
);

CREATE TABLE theaters_ranking(
    TheaterID int not null,
    RankingType enum('Daily', 'Monthly', 'Weekly', 'Weekend') not null,
    Ranking int not null,
    foreign key(TheaterID)
      references theaters(TheaterID) on delete cascade on update cascade
);

CREATE TABLE users(
    UserID int not null auto_increment,
    UserName varchar(50) not null,
    primary key(UserID)
);

CREATE TABLE comments(
    CommentID int not null auto_increment,
    UserID int not null,
    TheaterID int not null,
    Content varchar(255) null,
    Reply varchar(255) null,
    Likes int null,
    Image blob null,
    primary key(CommentID),
    foreign key(UserID)
      references users(UserID) on delete cascade on update cascade,
    foreign key(TheaterID)
      references theaters(TheaterID) on delete cascade on update cascade
);

CREATE TABLE request_info(
    CommentID int not null,
    TheaterID int not null,
    UpdateStatus boolean default null,
    foreign key(CommentID)
      references comments(CommentID) on delete cascade on update cascade,
    foreign key(TheaterID)
      references theaters(TheaterID) on delete cascade on update cascade
);
```

<br>

- **Database ERD**

![tig_ERD](https://user-images.githubusercontent.com/48443734/73184993-a474b800-4160-11ea-853f-eec0962a6e2c.png)
