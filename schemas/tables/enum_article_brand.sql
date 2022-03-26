create table if not exists enum_article_brand
(
    id                          serial          not null,
    short_name                  varchar(16)     not null,
    name                        varchar(64)     not null,
    is_enabled                  bool            not null    default true,
    created_at                  timestamptz     not null    default CURRENT_TIMESTAMP,
    updated_at                  timestamptz     not null    default CURRENT_TIMESTAMP,

    primary key (id),
    unique(short_name),
    unique(name)
);