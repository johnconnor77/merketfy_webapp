create table if not exists article
(
id                                      serial              not null,
    company_id                          integer             not null,
    article_category                    varchar             not null,
    article_type                        varchar             not null,
    article_brand                       varchar             not null,
    name                                varchar(128)        not null,
    url                                 varchar             not null,
    price                               double precision    not null,
    shipping_price                      double precision,
    rating                              double precision,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

