create table if not exists description
(
id                                      serial              not null,
    article_id                          integer             not null,
    description                         varchar(1024),
    attributes                          jsonb               not null    default '{}'::JSON,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

