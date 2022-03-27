create table if not exists favourite
(
    id                                  serial              not null,
    username                            varchar(64)         not null,
    password                            varchar(128)         not null,
    email                               varchar(64)         not null,
    birth_date                          date                not null,
    date_joined                         timestamptz         not null    default CURRENT_TIMESTAMP,
    last_login                          timestamptz         not null,
    is_admin                            boolean             not null    default FALSE,
    is_active                           boolean             not null    default TRUE,
    is_staff                            boolean             not null    default FALSE,
    is_superuser                        boolean             not null    default FALSE,
    removed_at                          timestamptz                     default null,
    created_at                          timestamptz         not null    default CURRENT_TIMESTAMP,
    updated_at                          timestamptz         not null    default CURRENT_TIMESTAMP,

    primary key (id)
);
