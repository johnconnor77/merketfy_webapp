create table if not exists company
(
    id                                  serial              not null,
    name                                varchar             not null,
    description                         varchar(1024)       not null,
    note                                varchar(1024),
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);

